import tkinter
from tkinter import *
import json

#parent class
class Page(tkinter.Frame):
    
   def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
    
   def show(self):
        self.lift()
    
