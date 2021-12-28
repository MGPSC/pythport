from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt
import sys

class BcryptEncrypt():
    """
    bcrypt_encrypt(password) -> takes in user password, inserts password to encryption scheme. To return hashed password, use .cook_hash().
    """
    def __init__(self, password):
        self.pass_scheme = b64encode(SHA256.new(password.encode()).digest())

    def cook_hash(self):
        master_hash = bcrypt(self.pass_scheme, 14)
        return master_hash
