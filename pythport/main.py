import tkinter as tk
from tkinter import ttk

from pythport.master_manager import MasterManager
from pythport.aes import AesEncrypt
from pythport.interface import login_screen
    
mm = MasterManager()

root = tk.Tk()
root.title("PythPort")
login_screen(root, mm)
root.mainloop()