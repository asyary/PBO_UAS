import random
import string

# Function to generate a random alphanumeric string of a specified length
def generate_random_alphanumeric(length=5, count=6):
    alphanumeric_codes = []
    for _ in range(count):
        # Select random characters from uppercase letters and digits
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        alphanumeric_codes.append(code)
    return alphanumeric_codes

# # Generate 6 random alphanumeric codes of 5 characters each
# generate_random_alphanumeric()