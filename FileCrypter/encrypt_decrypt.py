import random
from cryptography.fernet import Fernet
from pathlib import Path


KEY_LOCATION = f"{Path().home()}/AppData/Local/FileCrypter/key.txt"

def encrypt(text):
    return Fernet(key=get_key()).encrypt(text)


def decrypt(text):
    return Fernet(key=get_key()).decrypt(text)


def encrypt_file(path) -> None:
    with open(path, "rb") as plain_file:
        plain_text = plain_file.read()
        encrypted_text = encrypt(plain_text)
    with open(path, "wb") as plain_file:
        plain_file.write(encrypted_text)

def decrypt_file(path) -> None:
    with open(path, "rb") as encrypted_file:
        encrypted_text = encrypted_file.read()
        plain_text = decrypt(encrypted_text)
    with open(path, "wb") as encrypted_file:
        encrypted_file.write(plain_text)


def change_key(confirm=True):
    key = Fernet.generate_key()
    if confirm:
        print("""
This operation will change your global cypher key.
You won't be able to decode previously encoded files.
To continue enter 'y'
        """)
        if input("$  ").lower() == "y":
            with open(KEY_LOCATION, "wb") as file:
                file.write(key)


def get_key():
    with open(KEY_LOCATION, "rb") as file:
        return file.read()
