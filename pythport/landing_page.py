import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LandingPage():
    def __init__(self, root, pm):
        self.root = root
        self.pm = pm
        self.pw_entry = tk.StringVar()
        self.content = ttk.Frame(self.root)

        tv = ttk.Treeview(self)
        tv['columns'] = ('Name', 'Username', 'Email', 'Password')
        tv.heading('Name', text='Name')
        tv.column('Name', anchor='center', width=100)
        tv.heading('Username', text='Username')
        tv.column('Username', anchor='center', width=100)
        tv.heading('Email', text='Email')
        tv.column('Email', anchor='center', width=100)
        tv.heading('Password', text='Password')
        tv.column('Password', anchor='center', width=100)

        def render_tree(tree):
            with open("saved.json", "r") as f:
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
        tv.pack(side="left", fill="both", expand=True)
        # label = tk.Label(self, text="This is page 2")
        # label.pack(side="top", fill="both", expand=True)


        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)