from win1_code import Win1Code
from tkinter import *
from tkinter import ttk
from self_code import SelfCode
class NEO_API(SelfCode,Win1Code):
    def __init__(self):
        super().__init__()
        self.Button.config(command=self.Button_sub)
    def Button_sub(self):
        self.win1_new()
        self.withdraw()
    def win1_new (self):
        self.win1_fcn()
        self.Button1.config(command=self.Button_back)
    def Button_back(self):
        self.deiconify()
        self.win1.withdraw()

a=NEO_API()
a.mainloop()












































































