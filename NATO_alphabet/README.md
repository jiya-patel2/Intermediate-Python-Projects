# NATO Phonetic Alphabet Converter

A Python project that converts any user-entered word into its **NATO phonetic alphabet representation** using **pandas**, **dictionary comprehension**, and **exception handling**.

---

## 📖 Project Overview

This project reads NATO phonetic alphabet data from a CSV file and converts each letter of a user-entered word into its corresponding phonetic code word.

This project demonstrates good Python practices such as:

* Dictionary comprehension
* List comprehension
* Exception handling
* Function design
* CSV data processing

---

## ✨ Features

✔ Converts any valid word into NATO phonetic format
✔ Handles invalid characters using try-except
✔ Uses pandas for efficient CSV reading
✔ Clean modular function design
✔ User-friendly error messages

---

## 📂 Project Structure

```
INTERMEDIATE-PYTHON-PROJECTS
│
└── NATO-Alphabet-Project
    │
    ├── main.py
    ├── README.md
    │
    └── NATO_alphabet
        └── nato_phonetic_alphabet.csv
```

---

## ⚙️ Requirements

Make sure Python is installed.

Install required library:

```
pip install pandas
```

---

## ▶️ How To Run

### 1 Clone repository

```
git clone https://github.com/jiya-patel2/INTERMEDIATE-PYTHON-PROJECTS.git
```

### 2 Move into project folder

```
cd INTERMEDIATE-PYTHON-PROJECTS/NATO-Alphabet-Project
```

### 3 Run program

```
python main.py
```

---

## 🧠 Concepts Used

| Concept                  | Purpose                   |
| ------------------------ | ------------------------- |
| Pandas                   | Reading CSV file          |
| Dictionary comprehension | Creating phonetic mapping |
| List comprehension       | Generating output list    |
| Exception Handling       | Handling invalid input    |
| Functions                | Code organization         |

---

## 🛡️ Error Handling

If user enters numbers or symbols:

Example:

```
Enter a word: Code123
Sorry, only letters in the alphabet please.
```

The program safely asks again.

---

## 📷 Example Output

```
Enter a word: Python

Output:
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```
