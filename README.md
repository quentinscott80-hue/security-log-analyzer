# Python Security Log Analyzer

A beginner-friendly cybersecurity project built with Python that analyzes simulated login activity and identifies IP addresses with repeated failed login attempts.

## Features

- Reads login records from a text file
- Counts successful and failed login attempts
- Tracks failed login attempts by IP address
- Generates alerts for IP addresses with 3 or more failed attempts
- Skips blank or incomplete log entries

## Technologies Used

- Python 3
- File handling
- Dictionaries
- Loops and conditional statements
- Visual Studio Code

## Project Structure

```text
security-log-analyzer/
├── main.py
├── log.txt
└── README.md
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python3 main.py
```

## Example Output

```text
LOGIN SECURITY REPORT
---------------------------
Successful logins: 3
Failed logins: 5

FAILED LOGIN ATTEMPTS BY IP
---------------------------
192.168.1.15 - 4 failed attempts
192.168.1.25 - 1 failed attempts

SECURITY ALERTS
---------------------------
ALERT: 192.168.1.15 has 4 failed login attempts!
```

## How It Works

The program reads each login record and extracts the IP address and login status.

A dictionary tracks the number of failed attempts for each IP address.

If an address has 3 or more failed attempts, the program displays a security alert.

## Limitations

- Uses simulated login data, not live system logs
- Counts failures across the entire file rather than within a time window
- Does not confirm that a login attempt is malicious
- Designed for learning, not production security monitoring

## Future Improvements

- Add time-based detection
- Support additional log formats
- Export security reports
- Add configurable alert thresholds

## Purpose

I created this project to strengthen my Python programming, debugging, file processing, and introductory cybersecurity analysis skills.
