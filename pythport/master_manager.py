from pythport.bcrypt import BcryptEncrypt
import json

class MasterManager():
    """
    Initializes with a self.master_dict which references the master.json as a dictionary object.
    #### METHODS
    - `.create_master_hash(self, passphrase)` - takes in string, encrypts to a hash, then updates then master.json
    - `.validate_master_pwd(self, attempt)` - takes in string, compares against master_hash, returns Boolean. """

    def __init__(self):
        with open('assets/master.json', "r") as f:
            master_json = f.read()
            self.master_dict = json.loads(master_json)

    def create_master_hash(self, passphrase):
        bc = BcryptEncrypt(passphrase)
        hash = bc.cook_hash()
        self.master_dict["master"]["hash"] = hash.decode()
        with open('assets/master.json', "w") as f:
            f.write(json.dumps(self.master_dict))

    def validate_master_pwd(self, attempt):
        master_hash = self.master_dict["master"]["hash"].encode()
        validated = BcryptEncrypt.validate_pwd(attempt, master_hash)
        print("Validated:", validated)


if __name__ == "__main__":
    
    pass_hash = MasterManager.master_dict["master"]["hash"]

    if pass_hash is None:
        ## ON FIRST RUN (no stored password)
        passphrase = input("What would you like your password to be?\n> ")
        MasterManager.create_master_hash(passphrase)
    else:
        ## ANY OTHER RUN
        attempt = input("Please enter your password:\n> ")
        MasterManager.validate_master_pwd(attempt)
        