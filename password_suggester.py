import random
import string

def suggest_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+="

    all_chars = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)
