import random
import string

# Function to generate a random alphanumeric string of a specified length
def generate_random_alphanumeric(length=5, count=6):
    for _ in range(count):
        # Select random characters from uppercase letters and digits
        alphanumeric_codes = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return alphanumeric_codes

# generate_random_alphanumeric()