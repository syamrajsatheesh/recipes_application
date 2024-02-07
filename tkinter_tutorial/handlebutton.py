from tkinter import *


window = Tk()
window.geometry("1200x720")
window.title("Welcome")

def print1 ():
    print("Demo")

def exit1() :
    exit()

label1 = Label(window, text = 'abc', relief='solid', width=20, font=('arial', 19, 'bold'))
label1.pack(fill=BOTH, pady=10, padx=0, expand=False)

label2 = Label(window, text = 'xyz', relief='solid', width=20, font=('arial', 19, 'bold'))
label2.place(x=10, y=50)

button1 = Button(window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=print1)
#GROOVE, RIDGE, SUNKEN, RAISED
button1.place(x=10, y=100)



window.mainloop()
