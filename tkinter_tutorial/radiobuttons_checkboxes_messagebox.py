from tkinter import *
import tkinter.messagebox


window = Tk()
window.geometry(newGeometry="1200x720+10+10")
window.title("RECIPES")

var1 = StringVar()
ck1 = Checkbutton(window, text = "abc", variable=var1).place(x=10, y=120)
var2 = StringVar()
ck2 = Checkbutton(window, text = "abc", variable=var2).place(x=10, y=200)



var3 = StringVar()
r1 = Radiobutton(window, text = "abc", variable = var3, value='abc').place(x=100, y =420)
var4 = StringVar()
r2 = Radiobutton(window, text = "abc", variable = var4, value='abc').place(x=100, y =620)

tkinter.messagebox.showinfo("abshfc", 'sjhfsjf')


window.mainloop()