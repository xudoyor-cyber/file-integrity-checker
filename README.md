# 🔐 File Integrity Checker

A lightweight cybersecurity tool that detects file tampering using SHA-256 hashing.  
This project helps monitor sensitive files and alerts the user when a file is modified or deleted.

Designed as an educational cybersecurity project by **Sirojiddinov Xudoyor**, this tool demonstrates core concepts used in digital forensics and system security.

---

## 🚀 Features

- Tracks any file on your system  
- Detects:
  - ✔ MODIFIED files
  - ✔ DELETED files
  - ✔ Safe/unchanged files  
- Uses SHA-256 hashing  
- Stores file hashes in a local JSON database  
- Clean and professional CLI interface using `rich`

---

## 📂 Project Structure

file-integrity-checker/
│
├── file_integrity_checker.py # Main program
├── hashes.json # Stores file hashes
├── requirements.txt # Dependencies
└── .gitignore # Ignored files

---

## 🛠 Installation

1. Clone the repository:
git clone https://github.com/xudoyor-cyber/file-integrity-checker.git


2. Install dependencies:
pip install -r requirements.txt


3. Run the program:
python file_integrity_checker.py

---

## 📌 How It Works

1. You select a file to track  
2. The program calculates its SHA-256 hash  
3. The hash is stored in `hashes.json`  
4. When you run an integrity check, the program:
   - recalculates the file hash  
   - compares it with the original  
   - reports any changes

---

## 🧪 Example Output

File Integrity Checker

file.txt OK
config.cfg MODIFIED
secret.doc DELETED

---

## 🎯 Purpose

This project was created as part of my preparation for studying **Cybersecurity**.  
My goal is to develop tools that help prevent digital harm and improve security awareness in my community.

---

## 📎 Future Improvements

- Real-time file monitoring  
- Email alerts on changes  
- GUI version  
- Multi-folder integrity scans

---

## 📜 License

This project is open-source and available for learning and educational use.


