from .encrypt_decrypt import encrypt_file, decrypt_file
import os


def encrypt_directory(path, deep=False):

    for directory in os.listdir(os.path.join(os.getcwd(), path)):
        new_path = os.path.join(os.getcwd(), path, directory)
        if os.path.isfile(new_path):
            try:
                encrypt_file(new_path)
            except Exception:
                print("cannot encrypt file")
        elif deep:
            encrypt_directory(new_path, deep=True)

def decrypt_directory(path, deep=False):
    for directory in os.listdir(os.path.join(os.getcwd(), path)):
        new_path = os.path.join(os.getcwd(), path, directory)
        if os.path.isfile(new_path):
            try:
                decrypt_file(new_path)
            except Exception:
                print("cannot decrypt file")
        elif deep:
            decrypt_directory(new_path, deep=True)
