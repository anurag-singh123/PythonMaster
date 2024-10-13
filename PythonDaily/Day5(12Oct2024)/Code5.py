# Write a Python program that uses regular expressions (regex) to validate whether a given string is a valid email address.

import re

def is_valid_email(email):
    # Define the regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
emails = [
    "test@example.com",
    "invalid-email@.com",
    "user.name+tag+sorting@example.com",
    "user@domain.co",
    "user@domain",
    "user@domain..com"
]

for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")