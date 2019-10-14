from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import PIL

class _add_mission(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.make()

    def make(self):
        im2 = PIL.Image.open(r"D:\study\auto-arknights_\images\chapter_wz.png",'r') 
        img2 = ImageTk.PhotoImage(im2)
        self.button1=ttk.Button(self,image=img2)
        self.button1.grid(column=0,row=0)


a=_add_mission()
a.title("添加任务")
a.mainloop()