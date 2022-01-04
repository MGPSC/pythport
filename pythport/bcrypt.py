from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import bcrypt, bcrypt_check


class BcryptEncrypt():
    """
    BcryptEncrypt(password) -> Instantiates bcrypt encryption object. Takes in user password, inserts password to encryption scheme.
    #### METHODS
    - `.cook_hash()` - takes in a string and returns a hash.
    - `.validate_pwd(attempt_str, bcrypt_hash)` - takes in a string and stored hash, compares against algorithm, returns boolean.
    
    """
    def __init__(self, password):
        self.pass_scheme = b64encode(SHA256.new(password.encode()).digest())

    def cook_hash(self):
        master_hash = bcrypt(self.pass_scheme, 14)
        return master_hash

    @staticmethod
    def validate_pwd(pw_attempt, bcrypt_hash):
        try:
            attempt_scheme = b64encode(SHA256.new(pw_attempt.encode()).digest())
            bcrypt_check(attempt_scheme, bcrypt_hash)
            return True
        except ValueError:
            return False