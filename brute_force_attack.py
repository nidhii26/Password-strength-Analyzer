import hashlib
import string
from itertools import product
import time

def brute_force_attack(password):
    chars = string.ascii_lowercase
    target_hash = hashlib.md5(password.encode()).hexdigest()

    start_time = time.time()

    for length in range(1, 5):
        for guess in product(chars, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()

            if guess_hash == target_hash:
                return guess, round(time.time() - start_time, 2)

    return None, None
