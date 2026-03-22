# generate key
# file encrypt
# message encrypt
from cryptography.fernet import Fernet as fer
import fernet_cipher
import file_encrypt

def get_user_key():
    user_inp = input("Do you have a key? (Y)es | (N)o \n")
    if user_inp.lower() == "n":
        key = fer.generate_key()
        user_key = fer(key)
        print(key)
    elif user_inp.lower() == "y":
        user_key_ascii = input("Enter key: \n")
        user_key = user_key_ascii.encode('utf-8')
        user_key = fer(user_key)
    return user_key

def ent_user_key():

    user_key_ascii = input("Please enter key for decryption: \n")
    user_key = user_key_ascii.encode('utf-8')
    user_key = fer(user_key)
    return user_key

def fileencrypt():
    path = input("Enter path: \n")
    user_file_inp = input("Do you want to encrypt or decrypt? (E)| (D) \n")
    if user_file_inp.lower() == "d":
        key = ent_user_key()
    else:
        key = get_user_key()
    file_encrypt.FileOps.write_file(path,key,user_file_inp)

def message_encrypt(user_message):
    user_message_bytes = user_message.encode('utf-8')
    user_message_inp = input("Do you want to encrypt or decrypt? (E)| (D) \n")
    if user_message_inp.lower() == "e":
        key = get_user_key()
        print(fernet_cipher.Crypt.encrypt(user_message_bytes, key))
    elif user_message_inp.lower() == "d":
        key = ent_user_key()
        print(fernet_cipher.Crypt.decrypt(user_message_bytes, key))
    else:
        return "nothing"

def main():

    encrypt_choice = input("Do you want to work with a file or just a message: ")
    if encrypt_choice.lower() == "f":

        fileencrypt()
    elif encrypt_choice.lower() == "m":
        user_message = input("message you wnat to encrypt /decrypt: ")
        message_encrypt(user_message)

if __name__ == "__main__":
    main()
