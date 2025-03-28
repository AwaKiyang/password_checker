# Password Strength Checker

## Description
This is a Python script that evaluates the strength of a user-entered password based on several security criteria. The script checks for:
- Minimum length of 12 characters.
- Presence of at least 3 uppercase, lowercase, numeric, and special characters.
- Avoiding common words and previously used passwords (from a wordlist file).

## Features
- Reads a list of common passwords from `wordlist.txt`.
- Provides feedback on password strength (Weak, Medium, or Strong).
- Detects if a password contains common words or weak patterns.
- User-friendly prompts and error handling.

## Installation
1. Clone this repository or download the `password_checker.py` file.
2. Ensure you have Python installed (Python 3.x recommended).
3. (Optional) Provide a `wordlist.txt` file with common passwords for additional security checks.

## Usage
Run the script using:
```sh
python password_checker.py
```
Follow the on-screen instructions to enter a password and receive strength feedback.

## Example Output
```
**** Welcome to Password Strength Checker ****
Remember the following:
    - Password length must be at least 12 characters.
    - Must contain at least 3 uppercase, lowercase, numbers, and punctuation characters.
    - Avoid using common passwords or words.

Enter password to check: SecureP@ss123!
Uppercase: 3, Lowercase: 6, Numbers: 3, Punctuations: 2
Perfect strong password!
```

## Requirements
- Python 3.x
- A `wordlist.txt` file (optional) for checking common passwords.

## Contributing
Feel free to submit issues or pull requests to enhance this project.

## License
This project is licensed under the MIT License.

