# Password Strength Checker

This repository contains a Python script that evaluates the strength of a password based on several criteria, including length, uppercase and lowercase letters, digits, and special characters.

## Features

- **Password Length Check**: Ensures the password is at least 8 characters long.
- **Character Check**: Verifies the presence of:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters (!, @, #, $, %, ^, &, *, (, :, ", ?, >, /, ) )
- **Strength Classification**: Passwords are classified as:
  - `Strong`: If all criteria are met.
  - `Weak`: If fewer than 3 criteria are met.
  - `Moderate`: If the password meets 3 or 4 criteria.

## How to Use

1. Clone or download the repository.
2. Run the Python script and input a password when prompted.
3. The script will evaluate the password and output its strength.

```bash
$ python password_strength_checker.py
