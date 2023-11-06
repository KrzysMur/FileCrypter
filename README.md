
## FileCrypter

A simple CLI tool to encrypt and decrypt files.

## Requirements

 - Windows OS
 - Python 3.10 or newer

## Install

    git clone https://github.com/KrzysMur/FileCrypter

From your FileCrypter directory:

    pip install .

## How to use FileCrypter
		 

    from filecrypter.encrypt_decrypt import encrypt, decrypt

Functions `encrypt(text)` and `decrypt(text)` from encrypt_decrypt.py module take a "text" argument of "bytes" type.
Functions `encrypt_file(path)` and `decrypt_file(path)` from encrypt_decrypt.py module take a "path" argument of "string" type.

Function `change_key(confirm)`from encrypt_decrypt.py module generates new 32-bit key. Optional argument confirm has default value of True. It tells if the user has to confirm key change or not. Changing key makes the previously encrypted files not decryptable as old keys are not stored anywhere.

Default key location is C:/Users/[username]/AppData/Local/FileCrypter/key.txt



## CMD entry point

After installing the package on your device `filecrypter` cmd command is available. It takes no arguments and runs `main()`function from main.py module. 

 - `quit` - quits the program
 - `encrypt [file path]` - encrypts specified file
 - `decrypt  [file path]` - decrypts specified file
 - `key` - prints currently used key 
 - `cd [path]` - changes cwd to path
 - `pwd` - prints working directory
 - `chkey` - changes key; prompts to confirm operation
- `encryptdir [dir] [flag]` - encrypts directory dir; optional flag "-d" encrypts all subdirectorys of dir
- `decryptdir [dir] [flag]` - decrypts directory dir; optional flag "-d" decrypts all subdirectorys of dir
