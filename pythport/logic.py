# import bcrypt
# import aes
# import sys
# from pythport.aes import AesEncrypt
from pythport.bcrypt import BcryptEncrypt
# from base64 import b64encode
# from Crypto.Hash import SHA256
# from Crypto.Protocol.KDF import bcrypt
# from Crypto import Random
# from Crypto.Cipher import AES
import json

# master['hash'] = [bcrypt_hash] 


def create_master_hash(master_dict):
    passphrase = input("Please enter your desired password \n> ")
    bc = BcryptEncrypt(passphrase)
    hash = bc.cook_hash()
    master_dict["master"]["hash"] = hash.decode()
    with open('assets/master.json', "w") as f:
        f.write(json.dumps(master_dict))


def master_to_json():
    with open('assets/master.json', "r") as f:
        master_json = f.read()
        print("M JSON: ", master_json)
        master_dict = json.loads(master_json)
        print("dict:", master_dict)

    if master_dict["master"]["hash"] is None:
        create_master_hash(master_dict)
        
    # with open('../assets/master.json', "w") as f:
    #     json.dumps()

master_to_json()    
