from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.geometry("1200x720")
window.title("Welcome")

def print1 ():
    print("Demo")

def exit1() :
    exit()


"""img = Image.open("C:/Users/syamp/Documents/Recipe/im.png")
photo = ImageTk.PhotoImage(img)

lab = Label(image=photo)
lab.place(x=10, y=100)"""

label1 = Label(window, text = 'abc', relief='solid', width=20, font=('arial', 19, 'bold'))
label1.pack(fill=BOTH, pady=10, padx=0, expand=False)

label2 = Label(window, text = 'xyz', relief='solid', width=20, font=('arial', 19, 'bold'))
label2.place(x=10, y=50)

button1 = Button(window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=print1)
#GROOVE, RIDGE, SUNKEN, RAISED
button1.place(x=10, y=100)


fn = StringVar()
var = StringVar()

def print_some():
    fn1 = fn.get()
    var1 = var.get()
    print(fn1, var1)

entry1 = Entry(window,textvariable=fn)
entry1.place(x=240, y=240)


button2 = Button(window,text="D", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=print_some)
button2.place(x=100, y=100)

list1 = {"tsp", "Tbp"}
droplist = OptionMenu(window, var, *list1)
var.set("Select spoon")
droplist.config(width=15)
droplist.place(x=230,y=370)


window.mainloop()
