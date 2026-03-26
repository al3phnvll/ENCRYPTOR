from cryptography.fernet import Fernet as fer
import fernet_cipher
import file_encrypt
import argparse

# to check if file or message
# to encrypt or decrypt
    # decrypt - user enter key
    # encrypt - ask user for key
def get_key(key_str):
    if key_str is None:
        key = fer.generate_key()
        print(f"Generated key: {key.decode()}")
        return fer(key)
        
    else:
        key_str = key_str.encode('utf-8')

        return key_str

def encrypt_message(args):
    user_message_bytes = args.message.encode('utf-8')
    key = get_key(args.key)
    print(key)
    if args.action == "encrypt":
        result = fernet_cipher.Crypt.encrypt(user_message_bytes, key)
        print(f"Encrypted: {result}")
    elif args.action == "decrypt":
        result = fernet_cipher.Crypt.decrypt(user_message_bytes, key)
        print(f"Decrypted: {result}")

    

def encrypt_file(args):
    key = get_key(args.key)
    choice = args.action[0].upper()
    result = file_encrypt.FileOps.write_file(args.path, key, choice)
    print("Done")





def main():
    parser = argparse.ArgumentParser(description="Fernet encryption tool.")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    message_parser = subparsers.add_parser("message")
    message_parser.add_argument("action" , choices= ["encrypt" , "decrypt"])
    message_parser.add_argument("--message" , type = str, required=True)
    message_parser.add_argument("--key" , default=None)



    file_parser = subparsers.add_parser("file")
    file_parser.add_argument("action" , choices= ["encrypt" , "decrypt"])
    file_parser.add_argument("--path", required=True) 
    file_parser.add_argument("--key" , default=None)

    args = parser.parse_args()
    print("-----")
    print(args.key)
    print("-----")
    print("-----")

    
    if args.mode == "message":
        print(args.message)
        encrypt_message(args)
    elif args.mode == "file":
        encrypt_file(args)

if __name__ == "__main__":
    main()
