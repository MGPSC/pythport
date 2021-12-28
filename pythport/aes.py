# Implementation of the two-way encrypt/decrypt algos
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
import sys
# from Crypto.Protocol.KDF import bcrypt

class AesEncrypt():
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = SHA256.new(key.encode()).digest()
        
    def __pad(self, text):
        required_bytes = self.block_size - len(text) % self.block_size
        ascii_str = chr(required_bytes)
        padding = ascii_str * required_bytes
        padded_text = text + padding
        return padded_text

    @staticmethod
    def __unpad(text):
        last_character = text[len(text) - 1:]
        bytes_to_remove = ord(last_character)
        return text[:-bytes_to_remove]

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, plain_text):
        encrypted_text = b64decode(plain_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("UTF-8")
        return self.__unpad(plain_text)


# print(dir(hash))

# print(hash.hexdigest())
# Create a new AES cipher
# new_cipher(key, *args, **kwargs)

aes = AesEncrypt("password123")

encrypty = aes.encrypt("hello-world!")

print(encrypty)

aes = AesEncrypt("password123")

decrypty = aes.decrypt(encrypty)

print(decrypty)
