import os
from .encrypt_decrypt import encrypt_file, decrypt_file, get_key, change_key
from pathlib import Path
import subprocess


def main():
    #cd(Path.home())
    create_app_data_folder()
    while True:
        command = get_command_from_user()
        process_command(command)


def get_command_from_user():
    return input("$  ")


def process_command(command):
    match command.split():
        case ["quit"]:
            print("Quitting the program")
            quit()
        case ["encrypt", filename]:
            encrypt(filename)
        case ["decrypt", filename]:
            decrypt(filename)
        case ["key"]:
            print(get_key())
        case ["cd", path]:
            cd(path)
        case ["pwd"]:
            print(os.getcwd())
        case ["chkey"]:
            change_key()
        case _:
            print("command not recognized")


def cd(path):
    try:
        os.chdir(path)
    except Exception as e:
        print(f"ERROR: {e}")


def encrypt(filename):
    try:
        encrypt_file(filename)
    except Exception as e:
        print(f"ERROR: {e} during encryption process")
    else:
        print(f"File {filename} encrypted successfully")


def decrypt(filename):
    try:
        decrypt_file(filename)
    except Exception as e:
        print(f"ERROR: {e} during decryption process")
    else:
        print(f"File {filename} decrypted successfully")


def create_app_data_folder():
    app_data_dir = os.path.join(Path().home(), "AppData", "Local", "FileCrypter")
    if not os.path.exists(app_data_dir):
        os.mkdir(app_data_dir)
        cd(app_data_dir)
        file.write(change_key(confirm=False))


if __name__=="__main__":
    main()
