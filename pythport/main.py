import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pythport.master_manager import MasterManager
from pythport.pass_manager import PassManager
import json
from random import randint

# from pythport.login_screen import LoginPage
# from pythport.landing_page import LandingPage
 
#####
## MAIN LOGIC
#####

class PythPortMain(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.window = None
        self.mm = MasterManager()
        # self.root = tk.Tk()
        self.title("PythPort")
        # self.window = LoginPage(self, self.mm)
        # self.window.render_self()
        self.pm = None
        self.switch_frame(LoginPage)

    def set_main_pm(self, password):
        self.pm = PassManager(password)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self.window is not None:
            self.window.destroy()
        self.window = new_frame
        self.window.render_self()
        # self.window.pack()

    # def show_login_page(self):
    #     self.window = LoginPage(self, self.mm)
    #     self.window.render_self()
    #     #clear page/render page

    # def show_landing_page(self):
    #     self.window = LandingPage(self, self.pm)
        
    #     pass


#####
## LOGIN PAGE LOGIC
#####

class LoginPage(tk.Frame):
    """
    Instantiates with a tkinter root and instance of MasterManager (mm). Handles all login screen rendering and logic.
    
    #### METHODS
    
    - .submit() - ensures the newly created master password is encrypted and stored in master.json
    - .login() - 
    - .render_self() - renders 'create password' or 'log in' page dependent on whether or not a master password is stored in json.
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pw_entry = tk.StringVar()
        self.main = master
        # self.content = ttk.Frame(self.root)

    def submit(self):
        password = self.pw_entry.get()
        print(password)
        if len(password) > 8:
            self.main.mm.create_master_hash(password)
            messagebox.showinfo(title="Success!", message="Your password has been created.")
            self.main.switch_frame(LoginPage)
        else:
            messagebox.showerror(title="Oops!", message="Your password must contain at least eight (8) characters. Please enter a longer password.")

    def login(self):
        self.main.switch_frame(LandingPage)

    # @staticmethod
    # def clear_all(element):
    #     for item in element.winfo_children():
    #         item.destroy()
    #     element.destroy()

    def render_self(self):
        pass_hash = self.main.mm.master_dict["master"]["hash"]
        self.pw_entry = tk.StringVar()
        # self.clear_all(self)
        # self = ttk.Frame(self.root)
        self.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))

        # Common Parts
        warn_label = ttk.Label(self, text="DO NOT FORGET THIS PASSWORD.\nWithout your password, you data will be lost forever.", justify = "center")
        pw_label = ttk.Label(self, text="Password:", justify = "right")

        #Parts for no saved login
        if pass_hash is None:  
            pw_entry = ttk.Entry(self, textvariable=self.pw_entry)
            label = ttk.Label(self, text="Welcome to Pythport!\nLet's get you set up.", justify = "center")
            prompt_label = ttk.Label(self, text = 'Please enter your desired password (at least 8 characters).')
            submit_btn = ttk.Button(self, text="Create", command = self.submit)

        #Parts for existing saved login
        if pass_hash:
            pw_entry = ttk.Entry(self, textvariable=self.pw_entry, show="*")
            label = ttk.Label(self, text="Welcome to Pythport!\nLet's go!", justify = "center")
            prompt_label = ttk.Label(self, text = 'Please enter your password.')
            submit_btn = ttk.Button(self, text="Log In", command = self.login)

        #put the parts in a grid
        label.grid(column = 0, row = 0, columnspan = 2, pady=(10,10))
        prompt_label.grid(column = 0, row = 1, columnspan = 2, pady=(10,30))
        pw_label.grid(column=0, row = 2, pady=(0, 10))
        pw_entry.grid(column = 1, row = 2,pady=(0, 10))
        submit_btn.grid(column = 0, row=3, columnspan = 2, pady=(30,30))
        warn_label.grid(column = 0, row = 4, columnspan = 2, pady=(0,20))

######
## LandingPage Logic
######

class LandingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.main = master
        # self.root = root
        # self.pm = pm
        self.pw_entry = tk.StringVar()
        # self.content = ttk.Frame(self.root)

    def render_self(self):
        self.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))
        tv = ttk.Treeview(self)
        tv['columns'] = ('Name', 'Username', 'Email', 'Password')
        tv.heading('Name', text='Name')
        tv.column('Name', anchor='center', width=150)
        tv.heading('Username', text='Username')
        tv.column('Username', anchor='center', width=150)
        tv.heading('Email', text='Email')
        tv.column('Email', anchor='center', width=200)
        tv.heading('Password', text='Password')
        tv.column('Password', anchor='center', width=200)

        def render_tree(tree):
            with open("assets/saved.json", "r") as f:
                raw_json = f.read()
                pass_dict = json.loads(raw_json)

            for key in pass_dict:
                login = pass_dict[key]
                info = list(login.values())
                if info[4]:
                    tree.insert('', 'end', values=info[:4])
                else:
                    tree.insert('', 'end', values=info[:2] + ['*'*8, '*'*8])  
        render_tree(tv)
        tv['show'] = 'headings'
        # tv.pack(side="top", fill="both", expand=True)
        # label = tk.Label(self, text="This is page 2")
        # label.pack(side="top", fill="both", expand=True)


        self.Treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        tv.grid(column = 0, row = 0)

app = PythPortMain()
app.mainloop()