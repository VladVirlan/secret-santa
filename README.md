# 🎅 Secret Santa

A lightweight, Python-based Secret Santa allocation tool that randomly assigns participants and emails them their assignments, including their recipient's optional wishlist information.

Designed for small communities, parishes, families, clubs and other groups looking for a simple alternative to third-party Secret Santa platforms.

## ✨ Features

- Random allocation: Automatically assigns each participant another participant.
No self-assignment: Nobody can be assigned themselves.
- Personalised emails: Each participant receives an individual email containing their recipient's details.
- Wishlist integration: Includes optional wishlist information in assignment emails, automatically omitting unanswered questions.
- CSV input: Easily import participant information from Google Forms or another spreadsheet application.
- SMTP email delivery: Send assignments using your own email account and SMTP provider.
- Locally operated: Allocation and email generation are handled by a locally executed Python script.

## 📋 Wishlist information

Participants can optionally provide:

- Hobbies and interests
- Something they'd love to receive
- Something they'd rather not receive
- Favourite snacks or sweet treats
- Favourite colours
- Allergies or dietary requirements
- Anything else their Secret Santa should know

Only completed wishlist fields are included in the recipient's email.

## 🚀 Getting started

### Requirements

- Python 3.10 or newer
- An email account with SMTP access
- A CSV file containing participant information

No third-party Python packages are currently required.

#### 1. Clone the repository

```bash
git clone https://github.com/VladVirlan/secret-santa.git
```

```bash
cd secret-santa
```

#### 2. Prepare your participant list

Create a file named participants.csv.

Example:

```csv
name,email,hobbies,desired_gifts,avoid_gifts,favourite_snacks,favourite_colours,allergies,anything_else
Alice,alice@example.com,Reading and baking,Books and candles,Strong perfumes,Chocolate,Blue,Peanut allergy,
Bob,bob@example.com,Football and music,,,Crisps,Green,,
Charlie,charlie@example.com,Photography,Camera accessories,,Chocolate,Red,,
```

The name and email fields are required. All wishlist fields are optional.

You can export responses from Google Forms into Google Sheets and download them as CSV.

Ensure the CSV column headings match those expected by the script.

#### 3. Configure email settings

The default example uses Gmail SMTP:

```python
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
```

For Gmail, you will generally need to enable two-step verification and generate an App Password.

Other SMTP providers can be used by changing the host and port accordingly.

Security: Never commit email passwords, app passwords or other credentials to Git. Use environment variables or another secure method of storing credentials.

#### 4. Run the script

```bash
python secret_santa.py
```

The script will load participants, generate assignments and ask for confirmation before sending individual emails.

## 📧 Example assignment email

```text
Subject: 🎄 Your Secret Santa Assignment!

Hello Alice!

It's time for our parish Secret Santa!

Your assigned recipient is:

Bob

A little about them...

Hobbies and interests: Football and music
Favourite snacks: Crisps
Favourite colours: Green

Please keep your assignment a secret!

Happy gifting! 🎅
```

## 🔒 Privacy and security

This project is designed to minimise unnecessary sharing of participant information.

Assignments are sent individually rather than through group emails.
Wishlist information is only included in the assigned giver's email.
Participant information should be stored securely.
Email credentials should never be committed to the repository.
Allocation files, if retained, should be protected and deleted when no longer needed.

The organiser runs the allocation process and may have access to the assignment mapping. This is not currently a cryptographically trustless or fully decentralised allocation system.

## 🛠️ Potential future improvements

- [ ] HTML-formatted festive emails
- [ ] Participant exclusion rules (e.g. couples or household members)
- [ ] Test/dry-run mode
- [ ] Secure assignment persistence and email retry functionality
- [ ] Automatic CSV processing from Google Forms
- [ ] Duplicate registration detection
- [ ] Reallocation when participants withdraw
- [ ] Improved privacy-preserving allocation protocol

## 📜 Licence

This project is licensed under the MIT License. See LICENSE for details.

## 🎄 St. Cosmas' Canon for the Nativity

### Greek (Original)

```text
Χριστὸς γεννᾶται, δοξάσατε
Χριστὸς ἐξ οὐρανῶν, ἀπαντήσατε.
Χριστὸς ἐπὶ γῆς, ὑψώθητε.
ᾌσατε τῷ Κυρίῳ πᾶσα ἡ γῆ,
καὶ ἐν εὐφροσύνῃ, ἀνυμνήσατε λαοί,
ὅτι δεδόξασται.

Ῥεύσαντα ἐκ παραβάσεως,
Θεοῦ τὸν κατ' εἰκόνα γενόμενον,
ὅλον τῆς φθορᾶς ὑπάρξαντα,
κρείττονος ἑπταικότα θείας ζωῆς,
αὖθις ἀναπλάττει, ὁ σοφὸς Δημιουργός,
ὅτι δεδόξασται.

Ἰδὼν ὁ Κτίστης ὀλλύμενον,
τὸν ἄνθρωπον χερσίν, ὃν ἐποίησε,
κλίνας οὐρανοὺς κατέρχεται
τοῦτον δὲ ἐκ Παρθένου θείας ἁγνῆς,
ὅλον οὐσιοῦται, ἀληθείᾳ σαρκωθείς,
ὅτι δεδόξασται.

Σοφία λόγος καὶ δύναμις,
Υἱὸς ὢν τοῦ Πατρός, καὶ ἀπαύγασμα,
Χριστὸς ὁ Θεός, δυνάμεις λαθών,
ὅσας ὑπερκοσμίους, ὅσας ἐν γῇ,
καὶ ἐνανθρωπήσας, ἀνεκτήσατο ἡμᾶς·
ὅτι δεδόξασται.
```

### Greek (Transliteration)

```text
Christós gennátai, doxásate
Christós ex ouranón, apantísate.
Christós epí gís, ipsóthite.
Ásate tó Kyrío pása i yí,
kaí en effrosýni, animnísate laí,
óti dedóxastai.

Réfsanta ek paraváseos,
Theoú tón kat' ikóna yenómenon,
ólon tís fthorás ipárxanta,
kríttonos eptaikóta thías zoís,
afthis anaplátti, o sofós Dimiourgós,
óti dedóxastai.

Idón o Ktístis ollímenon,
tón ánthropon khersín, ón epíise,
klínas ouranoús katérkhetai
toúton dé ek Parthénou thías agnís,
ólon ousioútai, alithía sarkothís,
óti dedóxastai.

Sofía lógos kaí dýnamis,
Yiós ón toú Patrós, kaí apávgasma,
Christós o Theós, dinámeis lathón,
ósas iperkosmíous, ósas en yí,
kaí enanthropísas, anektísato imás:
óti dedóxastai.
```

### English Translation

```text
Christ is born, glorify Him
Christ from Heaven, go meet Him.
Christ on earth, be exalted.
Sing to the Lord, O world!
And praise Him in joy,
For He is glorified.

He has allegedly transgressed,
God of the created,
Subject to all the corruption, fell
From the divine life,
Him, the wise Creator redeems himself,
For He is glorified.

And the Creator seeing that
The men on earth were perishing
Descended from the heavens
To the divine Virgin Mary,
Taking on our flesh,
For He is glorified.

The wisdom and power,
And word of God, the Son of the Father,
Christ the God, unknown to the powers above,
Hidden from those on earth, in human form
Won back the human race,
For He is glorified.
```
