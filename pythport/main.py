import tkinter as tk
from tkinter import ttk

from pythport.master_manager import MasterManager
from pythport.pass_manager import PassManager
from pythport.login_screen import LoginPage
from pythport.landing_page import LandingPage
 
class PythPortMain():
    def __init__(self):
        self.mm = MasterManager()
        self.root = tk.Tk()
        self.root.title("PythPort")
        self.window = LoginPage(self.root, self.mm)
        self.window.render_self()
        self.pm = None
        self.root.mainloop()

    def set_main_pm(self, password):
        self.pm = PassManager(password)

    def show_login_page(self):
        self.window = LoginPage(self.root, self.mm)
        #clear page/render page
        pass

    def show_landing_page(self):
        self.window = LandingPage(self.root, self.pm)
        
        pass

app = PythPortMain()