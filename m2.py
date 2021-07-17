import os
import time
import tkinter
from tkinter import *
from typing import Sized

root = Tk()

class Application():    

    def __init__(self):
        self.root   = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("===== by: Namoradinho! ===== ")
        self.root.configure(background='black')
        self.root.geometry("700x700")



Application()