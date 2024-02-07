from tkinter import *
from PIL import Image, ImageTk





def exit_app():
    exit()

window = Tk()
window.geometry(newGeometry="1200x720+10+10")
window.title("RECIPES")

"""img = Image.open("C:/Users/syamp/Documents/Recipe/im.jpg")
photo = ImageTk.PhotoImage(img)

label2 = Label(image=img)"""

fn = StringVar()
var = StringVar()

def print_some():
    fn1 = fn.get()
    var1 = var.get()
    print(fn1, var1)

label1 = Label(window, text="Favourite Recipes",fg="white", bg="black", relief="solid", font=("arial",20,"bold"))
label1.pack(fill=BOTH, pady=10, padx=0, expand=False)

button1 = Button(window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"))
#GROOVE, RIDGE, SUNKEN, RAISED
button1.place(x=10, y=50)

button2 = Button(window,text="DELETE", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"))
button2.place(x=100, y=50)

entry1 = Entry(window,textvariable=fn)
entry1.place(x=240, y=240)

list1 = {"tsp", "Tbp"}
droplist = OptionMenu(window, var, *list1)
var.set("Select spoon")
droplist.config(width=15)
droplist.place(x=230,y=370)

button3 = Button(window,text="Quit", fg="white", bg="black", relief=GROOVE, font=("arial",14,"bold"), command=exit_app)
button3.place(x=10, y=650)

button4 = Button(window,text="PRINT", fg="white", bg="black", relief=GROOVE, font=("arial",14,"bold"), command=print_some)
button4.place(x=10, y=500)

window.mainloop()