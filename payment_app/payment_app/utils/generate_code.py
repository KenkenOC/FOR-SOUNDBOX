import random

def secret_key():
    return "EhnH4GzdjNLxPoEnElEiHvMuzRcv3bMK"

    
def generate_virtual_account():
    angka_random = str(random.randint(1000000000, 9999999999))
    va = f"VA{angka_random}"
    return va