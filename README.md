# Folder Analyzer

A simple Python command-line tool that recursively scans folders and provides a basic file summary.

## Features

- Folder path validation
- Recursive folder scanning
- File counting by extension
- File listing
- Handles files without extensions
- Allows the user to run the analyzer again

## Technologies

- Python
- pathlib
- collections.Counter

> **Note:** `pathlib` and `collections` are intentionally listed in `requirements.txt` for educational purposes. They are part of Python's standard library and normally do not need to be installed separately.

## How to Run

```bash
python main.py

Project Structure
Folder-Analyzer/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── Models/
    ├── Get_data.py
    ├── Scan_data.py
    └── Print_data.py

Author: M.Arham
Started Project: August 13, 2026
**Version:** v1.0