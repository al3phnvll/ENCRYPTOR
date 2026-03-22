from cryptography.fernet import Fernet as fer

class Crypt:
    # key = fer.generate_key()
    # fernet = fer(key)

    @staticmethod
    def encrypt(message_in_byte,key):
        try:
            enc_byte = key.encrypt(message_in_byte)
            enc_message = enc_byte.decode('utf-8')
            return enc_message
        except:
            print(f"Encryption failed: {0}")
            return None
    
    @staticmethod
    def decrypt(message_in_byte,key):
        try:
            enc_byte = key.decrypt(message_in_byte)
            enc_message = enc_byte.decode('utf-8')
            return enc_message
        except:
            print(f"Decryption failed: {0}")
            return None
    
    