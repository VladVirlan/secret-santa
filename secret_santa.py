import csv
import os
import random
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

# ----------------------------
# CONFIGURATION
# ----------------------------

load_dotenv()

CSV_FILE = "participants.csv"

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))


# ----------------------------
# LOAD PARTICIPANTS
# ----------------------------

with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
    participants = list(csv.DictReader(f))

if len(participants) < 2:
    raise ValueError("You need at least two participants.")

# Normalise participant details
for participant in participants:
    participant["name"] = participant["name"].strip()
    participant["email"] = participant["email"].strip()

emails = [p["email"].lower() for p in participants]
names = [p["name"] for p in participants]

if any(not name for name in names) or any(not email for email in emails):
    raise ValueError("Every participant needs a name and email.")

if len(set(emails)) != len(emails):
    raise ValueError("Duplicate email addresses detected.")


# ----------------------------
# PREVIEW MODE
# ----------------------------

mode = input("\nRun in preview mode? (yes/no): ").strip().lower()

if mode not in ("yes", "no"):
    raise ValueError("Please enter yes or no.")

PREVIEW_MODE = mode == "yes"

if PREVIEW_MODE:
    print("\n[PREVIEW MODE] Emails will be displayed, not sent.")

else:
    print("\n[LIVE MODE] Emails will be sent to participants.")

    if not SENDER_EMAIL or not SMTP_PASSWORD:
        raise ValueError("Missing SENDER_EMAIL or SMTP_PASSWORD in .env file.")

    SMTP_PASSWORD = SMTP_PASSWORD.replace(" ", "")


# ----------------------------
# GENERATE SECRET SANTA PAIRS
# ----------------------------

rng = random.SystemRandom()
recipients = participants.copy()

# Shuffle until nobody gets themselves
while True:
    rng.shuffle(recipients)

    if all(
        giver["email"].lower() != recipient["email"].lower()
        for giver, recipient in zip(participants, recipients)
    ):
        break


# ----------------------------
# WISHLIST PROCESSING
# ----------------------------


def clean(value):
    """Return cleaned text, or None if empty."""

    if value is None:
        return None

    value = str(value).strip()

    if not value:
        return None

    if value.lower() in ("nan", "none", "n/a"):
        return None

    return value


def build_wishlist(recipient):
    """Build a formatted wishlist containing only answered questions."""

    fields = [
        ("hobbies", "Hobbies and interests"),
        ("desired_gifts", "Something they'd love to receive"),
        ("avoid_gifts", "Something they'd rather NOT receive"),
        ("favourite_snacks", "Favourite snacks or sweet treats"),
        ("favourite_colours", "Favourite colours"),
        ("allergies", "Allergies or dietary requirements"),
        ("anything_else", "Anything else"),
    ]

    answers = []

    for field, label in fields:
        answer = clean(recipient.get(field))

        if answer:
            answers.append(f"- {label}: {answer}")

    if not answers:
        return "No wishlist information was provided."

    return "\n".join(answers)


# ----------------------------
# EMAIL GENERATION
# ----------------------------


def build_email(giver, recipient):
    """Generate an individual Secret Santa email."""

    wishlist = build_wishlist(recipient)

    return f"""
Hello {giver["name"]}! 🎄

It's time for our parish Secret Santa!

Your assigned recipient is:

    {recipient["name"]}

A little about them... 🎁

{wishlist}

Please keep your assignment a secret!

Remember to get them a thoughtful gift and bring it
to our agreed Christmas gathering.

Happy gifting!

Your Secret Santa Organiser 🎅
"""


def create_message(giver, recipient):
    """Create an email message for an individual participant."""

    msg = EmailMessage()

    msg["Subject"] = "🎄 Your Secret Santa Assignment!"
    msg["From"] = SENDER_EMAIL or "[PREVIEW - NO SENDER]"
    msg["To"] = giver["email"]

    msg.set_content(build_email(giver, recipient))

    return msg


# ----------------------------
# PREVIEW MODE
# ----------------------------

if PREVIEW_MODE:
    print("\n" + "=" * 60)
    print("SECRET SANTA EMAIL PREVIEW")
    print("=" * 60)

    for index, (giver, recipient) in enumerate(zip(participants, recipients), start=1):
        msg = create_message(giver, recipient)

        print(f"\n{'=' * 60}")
        print(f"EMAIL {index}/{len(participants)}")
        print(f"To: {giver['name']} <{giver['email']}>")
        print(f"{'=' * 60}")

        print(msg.get_content())

    print("\n" + "=" * 60)
    print("PREVIEW COMPLETE - NO EMAILS SENT")
    print("=" * 60)


# ----------------------------
# LIVE EMAIL DELIVERY
# ----------------------------

else:
    print(f"\nReady to email {len(participants)} participants.")

    confirm = (
        input("\nThis will send real emails to all participants. Continue? (yes/no): ")
        .strip()
        .lower()
    )

    if confirm != "yes":
        print("Cancelled. No emails sent.")
        raise SystemExit

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SMTP_PASSWORD)

        for index, (giver, recipient) in enumerate(
            zip(participants, recipients), start=1
        ):
            msg = create_message(giver, recipient)

            server.send_message(msg)

            print(f"[{index}/{len(participants)}] Email sent to {giver['name']}")

    print("\nAll Secret Santa emails have been sent! 🎄")
