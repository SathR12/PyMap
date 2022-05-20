import tkinter
from tkinter import *

import page
from page import *

sys.path.append(r"C:\Users\laks\Desktop\Tracker\maps")

from pyMap import *

class SignIn(Page): #Extends Page parent class
    font = ('Arial', 20)
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        title = Label(self, text = "Sign In", font = SignIn.font)
        title.pack(side = "top", fill = "both", expand = True)
        
#         submit = Button(self, text = "send verification code")
#         submit.pack(side = "top", fill = "both", expand = True)
        
        
  
class Verify(Page):
    font = ('Arial', 20)
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
            
        title = Label(self, text = "Verification Code", font = SignIn.font)
        title.pack(side = "top", fill = "both", expand = True)
        
        
class Success(Page):
    font = ('Arial', 20)
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Map(self)
        
        
        
       
        
    
    
    

        
        
    