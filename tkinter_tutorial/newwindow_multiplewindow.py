from tkinter import *
import tkinter.messagebox


window = Tk()
window.geometry(newGeometry="1200x720+10+10")
window.title("RECIPES")


def second_window():
    window2 = Tk()
    window2.title("REMEMBER")
    window2.geometry("250x250")
    label2 = Label(window2, text="fuck off", relief= 'solid', font = ('arial', 12, 'bold')).place(x=10, y=50)
    button2 = Button(window2,text="OFF", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"))
    button2.place(x=100, y=50) 

button1 = Button(window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=second_window)
#GROOVE, RIDGE, SUNKEN, RAISED
button1.place(x=10, y=50)




window.mainloop()