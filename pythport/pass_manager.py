from pythport.aes import AesEncrypt
import json

class PassManager():
    def __init__(self, master):
        self.crypto = AesEncrypt(master)
        with open("assets/saved.json", "r") as f:
            saved_json = f.read()
            self.saved_logs = json.loads(saved_json)
            print("self.saved_logs: ", self.saved_logs)

    # from GUI inputs: [{name: blah, url: www.blah.com, username: bb@email.com, password: 123abc}]
    
    def create_login(self, login_list):
        new_dict = login_list[0]
        new_dict['username'] = self.crypto.encrypt(new_dict['username'])
        new_dict['password'] = self.crypto.encrypt(new_dict['password'])

        print("new login:", new_dict)
        
        self.saved_logs.append(new_dict)

        print("updated logins:", self.saved_logs)

        with open('assets/saved.json', "w") as f:
            f.write(json.dumps(self.saved_logs, indent = 4))
            print("updated stored json")


    def retrieve_login(self):
        pass

new = [{'name': 'blah', 'url': 'www.blah.com', 'username': 'bb@email.com', "password": "123abc"}]

my_passes = PassManager("potato123")

my_passes.create_login(new)