# Email Invitation Generator 📧

This Python project automatically generates personalized invitation letters for multiple people using a template letter and a list of names.

The program reads a template letter, replaces the placeholder with each person's name, and creates individual invitation files.

---

## 📁 Project Structure

email_project
│
├── Input
│   ├── Letters
│   │   └── starting_letter.txt
│   │
│   └── Names
│       └── invited_names.txt
│
├── Output
│   └── ReadyToSend
│       ├── Adit_invitation.txt
│       ├── Ayan_invitation.txt
│       ├── Devakshi_invitation.txt
│       ├── Keshvi_invitation.txt
│       ├── Miral_invitation.txt
│       ├── Piyush_invitation.txt
│       ├── Samidha_invitation.txt
│       └── Sukriti_invitation.txt
│
└── main.py

---

## ⚙️ How It Works

1. The program reads names from:

Input/Names/invited_names.txt

2. It reads the template letter from:

Input/Letters/starting_letter.txt

Example template:

Dear [name],

I have planned to watch the new Jujutsu Kaisen movie this Sunday with friends .
You are invited to the same. We will have some food, movie time and also games after it.
Reach by sharp 4 p.m.

Hope you can make it!

Jiya 

3. The program replaces the placeholder:

[name]

with each person's name.

4. A new personalized letter is created for every name inside:

Output/ReadyToSend

---

## 📝 Example Output

Dear Keshvi,

I have planned to watch the new Jujutsu Kaisen movie this Sunday with friends .
You are invited to the same. We will have some food, movie time and also games after it.
Reach by sharp 4 p.m.

Hope you can make it!

Jiya 


Saved as:

Output/ReadyToSend/Keshvi_invitation.txt

---

## ▶️ How to Run the Project

Navigate to the project folder:

cd email_project

Run the Python script:

python main.py

Generated invitation letters will appear in:

Output/ReadyToSend

---

## 🧠 Python Concepts Used

- File Handling (open, read, write)
- String Replacement (replace)
- Loops
- File Paths
- Lists

---

## 💡 Key Idea

The placeholder [name] in the template letter allows dynamic personalization of invitations for multiple people.

Each name in the list generates a separate invitation file automatically.

