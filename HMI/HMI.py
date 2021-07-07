from tkinter import *
import os
win = Tk()
running = False

w = 800
h = 600
win.geometry(f"{w}x{h}")
win['bg'] = 'peach puff'
win.title("robot control")
win.iconbitmap("walli.ico")
win.resizable(False,False)

def start_engine(event):
        global running
        running = True
        print("start engine")

def stop_engine(event):
        global running
        running = False
        print("stop engine")


button1 = Button(win, text ="start robot", width = 7, height = 3)
button2 = Button(win, text = "stop robot", width = 7, height = 3)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button1.place(x=0, y=543)
button2.place(x= 743,y = 543)
button1.bind('<ButtonPress-1>', start_engine)
button2.bind('<ButtonPress-1>', stop_engine)

f_camera = Frame(win, height = 540, width = 720, bg = 'white').pack()





win.mainloop()