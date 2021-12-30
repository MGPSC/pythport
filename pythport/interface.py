import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

#poetry env 3.9.5
#pyenv shell --unset

def submit():
    password = pw_entry.get()
    print(password)
    # return password
    messagebox.showinfo(title="Success", message="Your password has been created.")
    print('you have confirmed')
# m_m= MasterManager()
# master = m_m.create_master_hash(password)

root = tk.Tk()
root.title("PythPort")
# root.geometry('400x400')
content = ttk.Frame(root)

content.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))

#define your parts
label = ttk.Label(content, text="Welcome to Pythport!\nLet's get you set up.", justify = "center")
prompt_label = ttk.Label(content, text = 'Please enter your desired password.')
warn_label = ttk.Label(content, text="DO NOT FORGET THIS PASSWORD.\nWithout your password, you data will be lost forever.", justify = "center")
pw_label = ttk.Label(content, text="Password:", justify = "right")
pw_entry = ttk.Entry(content)
submit_btn = ttk.Button(content, text="Submit", command= submit)

#put the parts in a grid
label.grid(column = 0, row = 0, columnspan = 2, pady=(10,10))
prompt_label.grid(column = 0, row = 1, columnspan = 2, pady=(10,30))
pw_label.grid(column=0, row = 2, pady=(0, 10))
pw_entry.grid(column = 1, row = 2,pady=(0, 10))
submit_btn.grid(column = 0, row=3, columnspan = 2, pady=(30,30))
warn_label.grid(column = 0, row = 4, columnspan = 2, pady=(0,20))

root.mainloop()