import re


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def validate_contact(contact):
    return contact.isdigit() and len(contact) == 10


def validate_password(password):
    return 6 <= len(password) <= 12


def validate_customer_name(name):
    return len(name.strip()) > 0 and len(name) <= 50
