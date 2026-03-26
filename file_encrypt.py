import os 
from fernet_cipher import Crypt

class FileOps:
    @staticmethod
    def read_file(path,key,choice):
        encrypted_list = []
        with open(path, "r") as f:
            lines = f.readlines()
        if choice.lower() == "e":
            for line in lines:
                clean = line.rstrip("\r\n")
                if not clean:
                    continue
                byte_line = clean.encode('utf-8')
                print(byte_line)
                encrypted_list.append(Crypt.encrypt(byte_line,key))
        elif choice.lower() == "d":
            for line in lines:
                clean = line.rstrip("\r\n")
                if not clean:
                    continue
                byte_line = clean.encode('utf-8')
                print(byte_line)
                encrypted_list.append(Crypt.decrypt(byte_line,key))
        for i in encrypted_list:
            print(i)
        return encrypted_list
    
    @staticmethod
    def write_file(path,key,choice):
        encrypted_list = FileOps.read_file(path,key,choice)
        with open(path , "w") as writefile:
            for i in encrypted_list:
                print(i)
                writefile.write(i)
                writefile.write("\n")


