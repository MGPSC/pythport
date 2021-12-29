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

def validate_master_pwd(master_dict):
    attempt = input("Please enter your password:\n> ")
    master_hash = master_dict["master"]["hash"].encode()

    validated = BcryptEncrypt.validate_pwd(attempt, master_hash)
    print("Validated:", validated)

def master_to_json():
    with open('assets/master.json', "r") as f:
        master_json = f.read()
        master_dict = json.loads(master_json)

    if master_dict["master"]["hash"] is None:
        create_master_hash(master_dict)

    else:
        validate_master_pwd(master_dict)
        
    # with open('../assets/master.json', "w") as f:
    #     json.dumps()

       
       

master_to_json()

# validate_master_pwd("potato123")

#{"master": {"hash": "$2a$14$FqQPPZGIOuc8tnLWprUjHu/9fdodsO0Pv1E19gYpjpffCosnrh.BC"}}
#{"master": {"hash": "$2a$14$9v.mWeDdTF7VjNXQQzlXregwcbjuJ.hOWjleEf2hJIBErdeYzwK.m"}}