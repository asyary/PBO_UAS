import re
from time import sleep
from datetime import datetime

def nik_handler(input_nik):
	"""Validates if the input is a properly formatted NIK."""
	if not re.match(r'^\d{16}$', input_nik):
		return False
	return True

def name_handler(input_text):
    """Validates if the input only contains allowed characters."""
    if not re.match(r'^[A-Za-z\.\'\-\s]{2,60}$', input_text):
        return False
    return True

def email_handler(input_email):
    """Validates if the input is a properly formatted email address."""
    if not re.match(r'^[\w\-]+@[\w\.-]+\.\w+$', input_email):
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
        return False
