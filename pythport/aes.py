# Implementation of the two-way encrypt/decrypt algos
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
# from Crypto.Protocol.KDF import bcrypt

class AesEncrypt():
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = SHA256.new(key.encode()).digest()
        
    def _pad(self, text):
        required_bytes = self.block_size - len(text) % self.block_size
        ascii_str = chr(required_bytes)
        padding = ascii_str * required_bytes
        padded_text = text + padding
        return padded_text

    def some_stuff(self):
        key = b"Pythport is cool"
        iv = Random.new().read(self.block_size)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        hashed = iv + cipher.encrypt(b"password123")
        return hashed
# print(dir(hash))

# print(hash.hexdigest())
# Create a new AES cipher
# new_cipher(key, *args, **kwargs)

AES = AesEncrypt("h")

print(len(AES._pad("woohoo")))

