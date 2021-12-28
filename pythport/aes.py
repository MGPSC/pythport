# Implementation of the two-way encrypt/decrypt algos
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import bcrypt

# hash = SHA256.new()
class bcrypt_encrypt():
    def __init__(self, password):
        self.pass_scheme = b64encode(SHA256.new(password).digest())

    def cook_hash(self):
        

class aes_encrypt():
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = 
        
    def some_stuff():
        key = b"Pythport is cool"
        iv = Random.new().read(self.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        hashed = iv + cipher.encrypt(b"password123")
        return hashed
# print(dir(hash))

# print(hash.hexdigest())
# Create a new AES cipher
# new_cipher(key, *args, **kwargs)


def request_password():
    password = input("Please enter your password: \n> ")
    if password == hashed:
        print("success")
        return
    print("FAIL")

request_password()