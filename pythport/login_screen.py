import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#poetry env 3.9.5
#pyenv shell --unset

# m_m= MasterManager()
# master = m_m.create_master_hash(password)
class LoginPage():
    """
    Instantiates with a tkinter root and instance of MasterManager (mm). Handles all login screen rendering and logic.
    
    #### METHODS
    
    - .submit() -
    - .login()-
    - .render_self()-
    """
    def __init__(self, root, mm):
        self.root = root
        self.mm = mm
        self.pw_entry = tk.StringVar()
        self.content = ttk.Frame(self.root)

    def submit(self):
        password = self.pw_entry.get()
        print(password)
        if len(password) > 8:
            self.mm.create_master_hash(password)
            messagebox.showinfo(title="Success!", message="Your password has been created.")
            self.render_self()
        else:
            messagebox.showerror(title="Oops!", message="Your password must contain at least eight (8) characters. Please enter a longer password.")

    def login(self):
        pass

    @staticmethod
    def clear_all(element):
        for item in element.winfo_children():
            item.destroy()
        element.destroy()

    def render_self(self):
        pass_hash = self.mm.master_dict["master"]["hash"]
        self.pw_entry = tk.StringVar()
        self.clear_all(self.content)
        self.content = ttk.Frame(self.root)
        self.content.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))

        # Common Parts
        warn_label = ttk.Label(self.content, text="DO NOT FORGET THIS PASSWORD.\nWithout your password, you data will be lost forever.", justify = "center")
        pw_label = ttk.Label(self.content, text="Password:", justify = "right")

        #Parts for no saved login
        if pass_hash is None:  
            pw_entry = ttk.Entry(self.content, textvariable=self.pw_entry)
            label = ttk.Label(self.content, text="Welcome to Pythport!\nLet's get you set up.", justify = "center")
            prompt_label = ttk.Label(self.content, text = 'Please enter your desired password (at least 8 characters).')
            submit_btn = ttk.Button(self.content, text="Create", command = self.submit)

        #Parts for existing saved login
        if pass_hash:
            pw_entry = ttk.Entry(self.content, textvariable=self.pw_entry, show="*")
            label = ttk.Label(self.content, text="Welcome to Pythport!\nLet's go!", justify = "center")
            prompt_label = ttk.Label(self.content, text = 'Please enter your password.')
            submit_btn = ttk.Button(self.content, text="Log In", command = self.login)

        #put the parts in a grid
        label.grid(column = 0, row = 0, columnspan = 2, pady=(10,10))
        prompt_label.grid(column = 0, row = 1, columnspan = 2, pady=(10,30))
        pw_label.grid(column=0, row = 2, pady=(0, 10))
        pw_entry.grid(column = 1, row = 2,pady=(0, 10))
        submit_btn.grid(column = 0, row=3, columnspan = 2, pady=(30,30))
        warn_label.grid(column = 0, row = 4, columnspan = 2, pady=(0,20))

