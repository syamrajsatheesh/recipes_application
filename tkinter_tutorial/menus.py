from tkinter import *
import tkinter.messagebox


window = Tk()
window.geometry(newGeometry="1200x720+10+10")
window.title("RECIPES")


menu = Menu(window)
window.config(menu=menu)

def exit1():
    exit()

def about1():
    tkinter.messagebox.showinfo("About", 'Welcome')


subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=about1)





window.mainloop()