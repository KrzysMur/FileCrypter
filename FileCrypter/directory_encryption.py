from .encrypt_decrypt import encrypt_file, decrypt_file
import os


def encrypt_directory(path):
    for directory in os.listdir(os.path.join(os.getcwd(), path)):
        new_path = os.path.join(os.getcwd(), path, directory)
        if os.path.isfile(new_path):
            encrypt_file(new_path)

def decrypt_directory(path):
    for directory in os.listdir(os.path.join(os.getcwd(), path)):
        new_path = os.path.join(os.getcwd(), path, directory)
        if os.path.isfile(new_path):
            decrypt_file(new_path)