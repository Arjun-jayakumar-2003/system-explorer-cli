# System Explorer CLI (Python)

A simple command-line tool to explore system-level information using Python.

## Features

- List files in the current or a custom directory  
- Show disk usage in a human-readable format  
- Display running processes (PID and name)  
- Log process snapshots with timestamps  

## Tech Stack

- Python 3  
- psutil  

## How to Run

1. Install dependencies:

   pip install -r requirements.txt

2. Run the script:

   python main.py

## Notes

- Some processes may be skipped due to permission restrictions  
- Log files are created in the directory where the script is executed  
