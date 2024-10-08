from tkinter import *
from tkinter import ttk
class SelfCode(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("tk")
        self.ws = self.winfo_screenwidth()
        pos_x=round((self.ws-805)/2)
        self.hs = self.winfo_screenheight()
        pos_y=round((self.hs-404)/2)
        self.geometry("805x404+"+str(pos_x)+"+"+str(pos_y))
        self.config(bg="black")
        self.attributes("-topmost",0)
        self.overrideredirect(0)
        self.image_Label=PhotoImage(master=self,file=r"C:/Users/Mahmoud Ragab/OneDrive/Desktop/NEO/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3drNjIyMDM4MjgtaW1hZ2Uta3A2Ym1jYmIuanBn.png")
        self.Label=Label(self,
                text="",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                image=self.image_Label
                )
        self.Project_Name=Label(self,
                text="NEO-AI for Space Science",
                bg="black",
                fg="white",
                font=("arial",22),
                )
        self.Entry1=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="",
                )
        self.Entry2=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="",
                )
        self.Entry3=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="",
                )
        self.Entry4=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="",
                )
        self.Entry5=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="fff",
                )
        self.Entry6=Entry(self,
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                bd=0,
                highlightcolor="blue",
                highlightbackground="black",
                highlightthickness=1,
                show="",
                )
        self.Button=Button(self,
                text="Submit",
                bg="white",
                fg="black",
                font=("arial",20),
                bd=5,
                highlightcolor=None,
                highlightbackground=None,
                activebackground="white",
                activeforeground="black",
                relief="raised",
                )
        self.image_NASA=PhotoImage(master=self,file=r"C:/Users/Mahmoud Ragab/Downloads/png-transparent-pdf-logo-nasa-insignia-outer-space-nasa-tv-television-blue-line-circle-removebg-preview (1).png")
        self.NASA=Label(self,
                text="Label",
                bg="#f0f0f0",
                fg="black",
                font=("arial",13),
                image=self.image_NASA
                )
        self.Label.place(x=-3,y=-7,width=805,height=407)
        self.Project_Name.place(x=404,y=7,width=375,height=49)
        self.Entry1.place(x=20,y=80,width=184,height=23)
        self.Entry2.place(x=20,y=120,width=184,height=23)
        self.Entry3.place(x=20,y=160,width=184,height=23)
        self.Entry4.place(x=20,y=200,width=184,height=23)
        self.Entry5.place(x=20,y=240,width=184,height=23)
        self.Entry6.place(x=20,y=280,width=184,height=23)
        self.Button.place(x=57,y=335,width=104,height=47)
        self.NASA.place(x=203,y=70,width=287,height=239)