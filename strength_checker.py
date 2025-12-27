import re

def check_strength(password):

    # Mandatory minimum length
    if len(password) < 12:
        return "WEAK"

    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_symbol = re.search(r"[!@#$%^&*()_+=-]", password)

    # Strong only if ALL conditions are present
    if has_lower and has_upper and has_digit and has_symbol:
        return "STRONG"
    else:
        return "MEDIUM"
