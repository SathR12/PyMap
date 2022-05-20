import tkinter
from tkinter import *

from page import *
from sign import *

import yagmail
import random
import sys
import json

sys.path.append(r"C:\Users\laks\Desktop\Tracker\maps")
sys.path.append(r"C:\Users\laks\Desktop\Tracker")

f = open(r"C:\Users\laks\Desktop\Tracker\users.json", "w")


from pyMap import *


count, email, SUCCESS, MAP = 0, 0, None, None


class Homepage(tkinter.Frame):
     def __init__(self, *args, **kwargs):
        global SUCCESS, MAP, b1, email
        tkinter.Frame.__init__(self, *args, **kwargs)
        
        SIGNIN = SignIn(self) 
        VERIFY = Verify(self)
        SUCCESS = Success(self)
                   
        buttonframe = Frame(self)
        container = Frame(self)
        
        buttonframe.pack(side = "bottom", fill = "both", expand = True)
        container.pack(side= "top", fill = "both", expand = True)
        
        SIGNIN.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
        VERIFY.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
        SUCCESS.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
    
          
        email = Entry(self, width = 50)
        email.insert(1, "Enter...")
        email.pack(side = "top", fill = "x", expand = True)
      
        b1 = Button(buttonframe, text = "Verify", command = lambda:[VERIFY.show(),
                                                                    Homepage.sendGmail(email.get()),
                                                                    Homepage.checkCode(email.get()),
                                                                    ])
                                                        
        b1.pack(side = "top", fill = "both", expand = True)
        
#         b1 = Button(buttonframe, text = "Verify", command = lambda:[Homepage.verifyCode(email.get()), b1.pack_forget()])
#         b1.pack(side = "top", fill = "both", expand = True)

        SIGNIN.show()
        
        
     def sendGmail(gmail):
        global random_code, count, MAP
        if count == 0:
            with yagmail.SMTP("authbot1237@gmail.com", "faex tqge arhi dfwj") as yag:
                random_code = random.randrange(100000, 999999)
                yag.send(gmail, "Your sign in code", [str(random_code)])
                count = 1
                hashed = [gmail]
                json.dump(hashed, f)
                f.close() 
        
                
     def checkCode(code):
        global random_code 
        if str(random_code) == code:
            b1.destroy()
            email.destroy()
            SUCCESS.show()
            
    
    
        
                               
if __name__ == "__main__":            
    root = Tk()
    root.geometry("1000x500")
    main = Homepage(root)
    main.pack(side = "top", fill = "both", expand = True)
    root.mainloop()

