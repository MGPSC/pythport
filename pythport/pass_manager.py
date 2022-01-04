import json
from pythport.aes import AesEncrypt

class PassManager():
    """
    Initiate with PassManager('your_master_password'). Manages saved website and login information.
    #### METHODS
    - `.create_login(login_list)` - takes a list of user inputs and updates saved.json
    - `.retrieve_logins()` - returns a dictionary containing all encrypted logins 
    - `.get_decrypted(string)` - queries logins by provided name string and returns decrypted version of match
    - `.get_encrypted(string) - queries logins by provided name string and returns encrypted version of match
    """

    def __init__(self, master):
        self.crypto = AesEncrypt(master)
        with open("assets/saved.json", "r") as f:
            saved_json = f.read()
            self.saved_logs = json.loads(saved_json)
    
    def create_login(self, login_list):
        new_dict = login_list[0]
        new_dict['username'] = self.crypto.encrypt(new_dict['username'])
        new_dict['password'] = self.crypto.encrypt(new_dict['password'])

        self.saved_logs[new_dict["name"]] = new_dict
        
        with open('assets/saved.json', "w") as f:
            f.write(json.dumps(self.saved_logs, indent = 4))


    def retrieve_logins(self):
        return self.saved_logs

    def delete_entry(self, site_name):

        del self.saved_logs[site_name]
        
        with open("assets/saved.json", "w") as f:
            f.write(json.dumps(self.saved_logs, indent=4))

    def get_decrypted(self, name):
        requested = self.saved_logs[name].copy()
        requested['username'] = self.crypto.decrypt(requested['username'])
        requested['password'] = self.crypto.decrypt(requested['password'])
        return requested

    def get_encrypted(self, name):
        return self.saved_logs[name]


if __name__ == "__main__":

    new = [{'name': 'spam', 'url': 'www.spam.com', 'username': 'bb@email.com', "password": "abc123"}]

    my_passes = PassManager("potato123")
    my_passes.create_login(new)