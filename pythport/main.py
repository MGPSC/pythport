import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pythport.master_manager import MasterManager
from pythport.pass_manager import PassManager
import json
from random import randint

#####
## MAIN APP LOGIC / STATE
#####

class PythPortMain(tk.Tk):
    """
    Intantiates tkinter GUI components. 
    #### METHODS
    - `.set_main_pm(password)` - takes a string, instantiates PassManager as a self.pm.
    - `.switch_frame(frame_class)` - takes a string, destroys frame and replaces with a new frame.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.window = None
        self.mm = MasterManager()
        self.title("PythPort")
        self.pm = None
        self.switch_frame(LoginPage)

    def set_main_pm(self, password):
        self.pm = PassManager(password)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.window is not None:
            self.window.destroy()
        self.window = new_frame
        self.window.render_self()
        
#####
## LOGIN PAGE
#####

class LoginPage(tk.Frame):
    """
    Instantiates with a tkinter root and instance of MasterManager (mm). Handles all login screen rendering and logic.
    
    #### METHODS
    
    - .submit() - ensures the newly created master password is encrypted and stored in master.json
    - .login() - evaluates login and redirects to LandingPage
    - .render_self() - renders 'create password' or 'log in' page dependent on whether or not a master password is stored in json.
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pw_entry = tk.StringVar()
        self.main = master

    def submit(self):
        password = self.pw_entry.get()
        if len(password) > 8:
            self.main.mm.create_master_hash(password)
            messagebox.showinfo(title="Success!", message="Your password has been created.")
            self.main.switch_frame(LoginPage)
        else:
            messagebox.showerror(title="Oops!", message="Your password must contain at least eight (8) characters. Please enter a longer password.")

    def login(self):
        password = self.pw_entry.get()
        if self.main.mm.validate_master_pwd(password):
            self.main.pm = PassManager(password)
            self.main.switch_frame(LandingPage)
        else:
            messagebox.showerror(title="Incorrect Password", message="Incorrect password!\nPlease try again!")


    def render_self(self):
        pass_hash = self.main.mm.master_dict["master"]["hash"]
        self.pw_entry = tk.StringVar()
        self.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))

        warn_label = ttk.Label(self, text="DO NOT FORGET THIS PASSWORD.\nWithout your password, you data will be lost forever.", justify = "center")
        pw_label = ttk.Label(self, text="Password:", justify = "right")

        if pass_hash is None:  
            pw_entry = ttk.Entry(self, textvariable=self.pw_entry)
            label = ttk.Label(self, text="Welcome to Pythport!\nLet's get you set up.", justify = "center")
            prompt_label = ttk.Label(self, text = 'Please enter your desired password (at least 8 characters).')
            submit_btn = ttk.Button(self, text="Create", command = self.submit)

        if pass_hash:
            pw_entry = ttk.Entry(self, textvariable=self.pw_entry, show="*")
            label = ttk.Label(self, text="Welcome to Pythport!\nLet's go!", justify = "center")
            prompt_label = ttk.Label(self, text = 'Please enter your password.')
            submit_btn = ttk.Button(self, text="Log In", command = self.login)

        label.grid(column = 0, row = 0, columnspan = 2, pady=(10,10))
        prompt_label.grid(column = 0, row = 1, columnspan = 2, pady=(10,30))
        pw_label.grid(column=0, row = 2, pady=(0, 10))
        pw_entry.grid(column = 1, row = 2,pady=(0, 10))
        submit_btn.grid(column = 0, row=3, columnspan = 2, pady=(30,30))
        warn_label.grid(column = 0, row = 4, columnspan = 2, pady=(0,20))

######
## LANDING PAGE
######

class LandingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.main = master
        self.hide = True
        self.pw_entry = tk.StringVar()
   
    def render_self(self):
        self.grid(column = 0, row = 0, columnspan = 4, rowspan = 4, padx=(50, 50), pady=(10, 50))
        tv = ttk.Treeview(self)
        tv['columns'] = ('Name', 'URL', 'Email', 'Password')
        tv.heading('Name', text='Name')
        tv.column('Name', anchor='center', width=150)
        tv.heading('URL', text='URL')
        tv.column('URL', anchor='center', width=150)
        tv.heading('Email', text='Email')
        tv.column('Email', anchor='center', width=200)
        tv.heading('Password', text='Password')
        tv.column('Password', anchor='center', width=200)
    
        def render_tree(tree):
            if tv.get_children():
                for item in tv.get_children():
                    tv.delete(item)

            pass_dict = self.main.pm.retrieve_logins()

            for key in pass_dict:
                login = self.main.pm.get_decrypted(key)
                info = list(login.values())
                if self.hide == False:
                    tree.insert('', 'end', values=info)
                elif self.hide == True:
                    tree.insert('', 'end', values=info[:2] + ['*'*8, '*'*8])  
     
        def toggle_hide(tv):

            if self.hide == True:
                self.hide = False
                render_tree(tv)
            elif self.hide == False:
                self.hide = True
                render_tree(tv)    

        def go_to_update():
            try:
                selected = tv.item(tv.focus())["values"]
                self.main.tree_selection = selected
                self.main.switch_frame(UpdateRemove)
            except IndexError:
                messagebox.showerror("No entry selected!", "Please select a login from the list to update/remove.")

        render_tree(tv)
        tv['show'] = 'headings'
        
        self.Treeview = tv
        tv.grid(column = 0, row = 1, columnspan=4)

        add_new_btn = ttk.Button(self, text="Add New", command = lambda: self.main.switch_frame(AddNewLogin))
        add_new_btn.grid(column=0, row=0)


        show_hide_btn = ttk.Button(self, text="Show/Hide", command = lambda: toggle_hide(tv))
        show_hide_btn.grid(column=1, row=0)

        pass_gen_btn = ttk.Button(self, text="Generate Random Password", command = lambda: self.main.switch_frame(GenPassword))
        pass_gen_btn.grid(column=2, row= 0)

        update_btn = ttk.Button(self, text="Update/Remove", command = go_to_update)
        update_btn.grid(column=3, row= 0)
        
######
## ADD NEW LOGIN
######

class AddNewLogin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.main = master
        self.new_name = tk.StringVar()
        self.new_url = tk.StringVar()
        self.new_username = tk.StringVar()
        self.new_pwd = tk.StringVar()

    def handle_save(self):
        new = [{'name': self.new_name.get(), 'url': self.new_url.get(), 'username': self.new_username.get(), "password": self.new_pwd.get()}]
        self.main.pm.create_login(new)
        self.main.switch_frame(LandingPage)

    def render_self(self):
        self.grid(column = 0, row = 0)

        title_label = ttk.Label(self, text = "Create New Login")

        name_label = ttk.Label(self, text = "Site:")
        name_entry = ttk.Entry(self, textvariable=self.new_name)
        url_label = ttk.Label(self, text = "URL:")
        url_entry = ttk.Entry(self, textvariable=self.new_url)
        username_label = ttk.Label(self, text = "Username:")
        username_entry = ttk.Entry(self, textvariable=self.new_username)
        pwd_label = ttk.Label(self, text = "Password:")
        pwd_entry = ttk.Entry(self, textvariable=self.new_pwd)

        create_btn = ttk.Button(self, text="Save", command=self.handle_save)
        cancel_btn = ttk.Button(self, text="Cancel", command = lambda: self.main.switch_frame(LandingPage))

        title_label.grid(column=0, row=0, columnspan=5)

        name_label.grid(column=1, row=1, columnspan=2)
        name_entry.grid(column=3, row=1, columnspan=3)
        url_label.grid(column=1, row=2, columnspan=2)
        url_entry.grid(column=3, row=2, columnspan=3)
        username_label.grid(column=1, row=3, columnspan=2)
        username_entry.grid(column=3, row=3, columnspan=3)
        pwd_label.grid(column=1, row=4, columnspan=2)
        pwd_entry.grid(column=3, row=4, columnspan=3)

        create_btn.grid(column = 3, row=5, pady=(20,20))
        cancel_btn.grid(column=4, row=5, pady=(20,20))

######
## UPDATE / REMOVE
######

class UpdateRemove(tk.Frame):
    """Instantiates the update/remove tkinter frame."""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.main = master
        self.login = self.main.pm.get_decrypted(self.main.tree_selection[0])
        self.new_url = tk.StringVar()
        self.new_username = tk.StringVar()
        self.new_pwd = tk.StringVar()

    def delete_login(self):
        name = self.login["name"]
        #TODO:Find way to integrate John Cena
        warn_response = messagebox.askquestion("Delete Login Requested", f"Are you sure you want to delete your login for {name}? Login information for this entry will be permanently deleted!", icon='warning')
        if warn_response == 'yes':
            self.main.pm.delete_entry(self.login["name"])
            self.main.switch_frame(LandingPage)
            
    def update_login(self):
        name = self.login["name"]
        updated = [{'name': self.login["name"], 'url': self.new_url.get(), 'username': self.new_username.get(), "password": self.new_pwd.get()}]
        self.main.pm.create_login(updated)
        messagebox.showinfo("Login Updated", f"Login information for {name} updated!")
        self.main.switch_frame(LandingPage)
        
    def render_self(self):
        self.grid(columnspan=5)

        #components
        title = ttk.Label(self, text="Update Login Information")

        name = ttk.Label(self, text=self.login["name"])

        url_label = ttk.Label(self, text = "URL:")
        current_url_label = ttk.Label(self, text = self.login["url"])
        new_url_entry = ttk.Entry(self, textvariable=self.new_url)
        new_url_entry.insert(0, self.login["url"])
        
        username_label = ttk.Label(self, text = "Username:")
        current_username_label = ttk.Label(self, text = self.login["username"])
        new_username_entry = ttk.Entry(self, textvariable=self.new_username)
        new_username_entry.insert(0, self.login["username"])

        pwd_label = ttk.Label(self, text = "Password:")
        current_pwd_label = ttk.Label(self, text = self.login['password'])
        new_pwd_entry = ttk.Entry(self, textvariable=self.new_pwd, show="*")
        new_pwd_entry.insert(0, self.login['password'])

        save_btn = ttk.Button(self, text="Update", command=self.update_login)
        cancel_btn = ttk.Button(self, text="Cancel", command=lambda:self.main.switch_frame(LandingPage))
        delete_btn = ttk.Button(self, text="Delete", command=self.delete_login)

        #positions
        title.grid(row=0, column=0, columnspan=3)

        name.grid(row=1, column=0, columnspan=3, pady=5)

        url_label.grid(row=2, column=1)
        current_url_label.grid(row=2, column=2, columnspan=2)
        new_url_entry.grid(row=3, column=2, columnspan=2)

        username_label.grid(row=4, column=1)
        current_username_label.grid(row=4, column=2, columnspan=2)
        new_username_entry.grid(row=5, column=2, columnspan=2)

        pwd_label.grid(row=6, column=1)
        current_pwd_label.grid(row=6, column=2, columnspan=2)
        new_pwd_entry.grid(row=7, column=2, columnspan=2)

        delete_btn.grid(row=8, column=1)
        save_btn.grid(row=8, column=2, padx=(30,3))
        cancel_btn.grid(row=8, column=3)

######
## GENERATE PASSWORD
######

class GenPassword(tk.Frame):
    """Instantiates the random password generator frame in tkinter. """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
    
    def render_self(self):    
        
        self.pack()

        def new_pass():
            pw_entry.delete(0, tk.END)
            pw_length = int(my_entry.get())
            my_pass = ''

            for _ in range (pw_length):
                my_pass += chr(randint(33,126))
            pw_entry.insert(0, my_pass)


        def clipb():
            self.clipboard_clear()
            self.clipboard_append(pw_entry.get())

        lf = tk.LabelFrame(self, text="How Many Characters?")
        lf.pack(pady=20)

        my_entry = tk.Entry(lf, font=("Helvetica", 24))
        my_entry.insert(0, "8")
        my_entry.pack(pady=20, padx=20)

        pw_entry = tk.Entry(self, text='', font=("Helvetica", 24), bd=0, bg="#000000")
        pw_entry.pack(pady=20)

        my_frame = tk.Frame(self)
        my_frame.pack(pady=20)

        my_button = tk.Button(self, text= "Generate New Password", command= new_pass)
        my_button.pack(padx=10, pady=10)

        back_button = tk.Button(self, text= "Back", command = lambda: self.master.switch_frame(LandingPage))
        back_button.pack(padx= 30, pady= 10)

        clip_button = tk.Button(self, text="Copy To Clipboard", command= clipb)
        clip_button.pack(padx=20, pady=10)


app = PythPortMain()
app.eval('tk::PlaceWindow . center')
app.mainloop()



