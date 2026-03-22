import os 
from fernet_cipher import Crypt

class FileOps:
    @classmethod
    def read_file(cls,path,key,choice):
        encrypted_list = []
        with open(path, "r") as f:
            lines = f.readlines()
        if choice.lower() == "e":
            for line in lines:
                byte_line = line.encode('utf-8')
                print(Crypt.encrypt(byte_line, key))
                encrypted_list.append(Crypt.encrypt(byte_line,key))
        elif choice.lower() == "d":
            for line in lines:
                byte_line = line.encode('utf-8')
                print(Crypt.decrypt(byte_line,key))
                encrypted_list.append(Crypt.decrypt(byte_line,key))
        return encrypted_list
    
    @classmethod
    def write_file(cls,path,key,choice):
        encrypted_list = FileOps.read_file(path,key,choice)
        with open(path , "w") as writefile:
            for i in encrypted_list:
                print(i)
                writefile.write(i)
                writefile.write("\n")



