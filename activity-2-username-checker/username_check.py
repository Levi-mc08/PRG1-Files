"""
Username Validator

Reads a file of usernames, checks each one, and appends the result
to a log file. A working program: nothing here is missing.
"""

import datetime
import os

INPUT_FILE = "./test_usernames.txt"
OUTPUT_FILE = "./username_validation_log.txt"

os.remove(OUTPUT_FILE)

def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def is_valid_username(username):
    clean_username = username.strip()
    return len(clean_username) > 3

def check_username(username):
    is_valid = is_valid_username(username)

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        result = "Valid" if is_valid else "Invalid"
        current_time = get_current_datetime_formatted()
        stripped_version = username.strip()
        f.write(f"{current_time} - Username: '{username}' --> '{stripped_version}' - {result}\n")

    return is_valid


def read_usernames_from_file(filename):
    with open(filename, "r") as f:
        return f.read()


username_data = read_usernames_from_file(INPUT_FILE)
usernames = username_data.split("\n")

print("Checking usernames from file:")
for username in usernames:
    result = check_username(username)
    print(f"'{username}' --> {result}")
