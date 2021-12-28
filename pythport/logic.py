# import bcrypt
# import aes
# import sys
# from pythport.aes import AesEncrypt
# from pythport.bcrypt import BcryptEncrypt
# from base64 import b64encode
# from Crypto.Hash import SHA256
# from Crypto.Protocol.KDF import bcrypt
# from Crypto import Random
# from Crypto.Cipher import AES
import json

master = {}
master['hash'] = [bcrypt_hash] 


def master_to_json(bcrypt_hash):
    
    with open('../assets/master.json', "w") as f:
        json.dumps()

    