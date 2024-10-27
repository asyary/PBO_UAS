import re
from time import sleep
from datetime import datetime

def text_handler(input_text):
    """Validates if the input only contains letters and spaces."""
    if not re.match(r'^[a-zA-Z\s]+$', input_text):  # Restrict to letters and spaces
        print("\nNama harus berisi huruf") #kalo masih pake CLI idk kalo pake GUI
        sleep(0.5)
        return False
    return True

def email_handler(input_email):
    """Validates if the input is a properly formatted email address."""
    if not re.match(r'^[\w\-]+@[\w\.-]+\.\w+$', input_email):  # Basic email pattern
        print("\nEmail tidak valid")
        sleep(0.5)
        return False
    return True

def phone_handler(input_phone):
    """Validates if the input is a properly formatted phone number."""
    if not re.match(r'^\+?\d{9,15}$', input_phone):  # Allows + at the start and 9-15 digits
        print("\nNomor telepon tidak valid")
        sleep(0.5)
        return False
    return True

def date_handler(input_date):
    """Validates if the input is a date in DD-MM-YYYY format."""
    try:
        datetime.strptime(input_date, '%d-%m-%Y')
        return True
    except ValueError:
        print("\nTanggal tidak valid. Gunakan format DD-MM-YYYY")
        sleep(0.5)
        return False

def numeric_handler(input_value, min_value=None, max_value=None):
    """Checks if the input is a number, optionally within a specified range."""
    try:
        value = float(input_value)
        if min_value is not None and value < min_value:
            print(f"\nNilai harus lebih besar atau sama dengan {min_value}")
            return False
        if max_value is not None and value > max_value:
            print(f"\nNilai harus lebih kecil atau sama dengan {max_value}")
            return False
        return True
    except ValueError:
        print("\nInput harus berupa angka")
        sleep(0.5)
        return False
