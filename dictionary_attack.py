import hashlib
import time

def dictionary_attack(password):
    target_hash = hashlib.md5(password.encode()).hexdigest()
    start_time = time.time()

    with open("common_passwords.txt", "r") as file:
        for word in file:
            word = word.strip()
            word_hash = hashlib.md5(word.encode()).hexdigest()

            if word_hash == target_hash:
                end_time = time.time()
                return word, round(end_time - start_time, 2)
    return None, None
