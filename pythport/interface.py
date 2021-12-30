import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#poetry env 3.9.5
#pyenv shell --unset



# m_m= MasterManager()
# master = m_m.create_master_hash(password)
def login_screen(root, mm):

    pass_hash = mm.master_dict["master"]["hash"]

    def submit():
        password = pw_entry.get()
        print(password)
        if len(password) > 8:
            mm.create_master_hash(password)
            messagebox.showinfo(title="Success!", message="Your password has been created.")
        else:
            messagebox.showerror(title="Oops!", message="Your password must contain at least eight (8) characters. Please enter a longer password.")

    def login():
        pass

    # root = tk.Tk()
    # root.title("PythPort")

    content = ttk.Frame(root)
    content.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))

# Common Parts
    pw_entry = ttk.Entry(content)
    warn_label = ttk.Label(content, text="DO NOT FORGET THIS PASSWORD.\nWithout your password, you data will be lost forever.", justify = "center")
    pw_label = ttk.Label(content, text="Password:", justify = "right")

#Parts for no saved login
    if pass_hash is None:  
        label = ttk.Label(content, text="Welcome to Pythport!\nLet's get you set up.", justify = "center")
        prompt_label = ttk.Label(content, text = 'Please enter your desired password (at least 8 characters).')
        submit_btn = ttk.Button(content, text="Create", command = submit)

#Parts for existing saved login
    if pass_hash:
        label = ttk.Label(content, text="Welcome to Pythport!\nLet's go!", justify = "center")
        prompt_label = ttk.Label(content, text = 'Please enter your password.')
        submit_btn = ttk.Button(content, text="Log In", command = login)

    #put the parts in a grid
    label.grid(column = 0, row = 0, columnspan = 2, pady=(10,10))
    prompt_label.grid(column = 0, row = 1, columnspan = 2, pady=(10,30))
    pw_label.grid(column=0, row = 2, pady=(0, 10))
    pw_entry.grid(column = 1, row = 2,pady=(0, 10))
    submit_btn.grid(column = 0, row=3, columnspan = 2, pady=(30,30))
    warn_label.grid(column = 0, row = 4, columnspan = 2, pady=(0,20))

