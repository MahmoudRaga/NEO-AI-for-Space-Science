from tkinter import *
from tkinter import ttk
class Win1Code():
    def win1_fcn(self):
        self.win1=Toplevel()
        self.win1.title("tk")
        self.ws = self.win1.winfo_screenwidth()
        pos_x=round((self.ws-805)/2)
        self.hs = self.win1.winfo_screenheight()
        pos_y=round((self.hs-404)/2)
        self.win1.geometry("805x404+"+str(pos_x)+"+"+str(pos_y))
        self.win1.config(bg="white")
        self.win1.attributes("-topmost",0)
        self.win1.overrideredirect(0)
        self.image_Label1=PhotoImage(master=self.win1,file=r"C:/Users/Mahmoud Ragab/OneDrive/Desktop/NEO/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3drNjIyMDM4MjgtaW1hZ2Uta3A2Ym1jYmIuanBn.png")
        self.Label1=Label(self.win1,
                text="",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                image=self.image_Label1
                )
        self.Entry1=Entry(self.win1,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                highlightthickness=1,
                show="",
                )
        self.Button1=Button(self.win1,
                text="Back",
                bg="#f0f0f0",
                fg="black",
                font=("arial",20),
                bd=0,
                highlightcolor=None,
                highlightbackground=None,
                activebackground="white",
                activeforeground="black",
                relief="flat",
                )
        self.Label1.place(x=-4,y=-2,width=805,height=413)
        self.Entry1.place(x=4,y=10,width=779,height=58)
        self.Button1.place(x=353,y=334,width=86,height=43)