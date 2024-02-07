from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import os
from tkinter import ttk
import pickle
from tkinter import scrolledtext



# Create a list of items
items = [f"Item {i}" for i in range(1, 21)]

def exit_app():
    exit()

def about_app():
    tkinter.messagebox.showinfo("About", 'This is a custom-made app to record and view food recipes')


window1 = Tk()
window1.geometry(newGeometry="500x400+10+10")
window1.title("MY RECIPES")

name = StringVar()
text_variable = StringVar()

"""current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "im.png")
img = Image.open(image_path)
tk_img = ImageTk.PhotoImage(img)
img_label = Label(window1, image=tk_img)
img_label.pack()"""

title_app = Label(window1, text="Favourite Recipes",fg="white", bg="black", relief="solid", font=("arial",20,"bold"))
title_app.pack(fill=BOTH, pady=10, padx=0, expand=False)

def view_recipe_window(event):

    window2 = Tk()
    window2.title("REMEMBER")
    window2.geometry("1000x500")
    label2 = Label(window2, text="", relief= 'solid', font = ('arial', 12, 'bold')).place(x=10, y=50)
    close_button1 = Button(window2,text="Close", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=exit_app)
    close_button1.place(x=200, y=200)
    save_button = Button(window2,text="Save", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"))
    save_button.place(x=10, y=200)


def add_recipe_window():

    window3 = Tk()
    window3.title("New Recipe")
    window3.geometry("1000x500")

    recipe_name = Label(window3, text="Recipe name",fg="black", font=("arial",12))
    recipe_name.place(x=10, y=20)

    recipe_name_entry = Entry(window3,textvariable=name)
    recipe_name_entry.place(x=150, y=20)

    fn1 = name.get()
    if fn1 in items:
        tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')

    steps = Label(window3, text="Steps",fg="black", font=("arial",12))
    steps.place(x=10, y=100)

    large_text = scrolledtext.ScrolledText(window3, wrap=WORD, width=50, height=10)
    large_text.place(x=150, y=100)

    save_button = Button(window3,text="Save", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=save_content(large_text))
    save_button.place(x=100, y=200)


def save_content(large_text):
        # Retrieve the text from the scrolled text box and assign it to the variable
     text_variable.set(large_text.get("1.0", END))
     print(text_variable)

def save_data_to_dat(file_path, data):
    try:
        # Load existing data from the pickle file
        with open(file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except (FileNotFoundError, EOFError):
        # Handle the case where the file is not found or is empty
        existing_data = {}

    # Append new data to the existing data
    key = list(data.keys())
    existing_data[key[0]] = data[key[0]]

    # Write the updated data back to the pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(existing_data, file)

def load_data_from_dat(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def menu_app(window):
    
    menu = Menu(window)
    window.config(menu=menu)

    subm1 = Menu(menu)
    menu.add_cascade(label="File", menu=subm1)
    subm1.add_command(label="Exit", command=exit_app)

    subm2 = Menu(menu)
    menu.add_cascade(label="Option", menu=subm2)
    subm2.add_command(label="About", command=about_app)

menu_app(window1)

def add_delete_button(window):
    add_button = Button(window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=add_recipe_window)
    add_button.place(x=10, y=50)

    delete_button = Button(window,text="DELETE", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"))
    delete_button.place(x=100, y=50)

add_delete_button(window1)

def items_box(window):

    box_frame = Frame(window, width=50, height=20)
    box_frame.place(x=10, y=100)


    # Create a Tkinter listbox
    listbox = Listbox(box_frame, selectmode=SINGLE)

    # Insert items into the listbox
    for item in items:
        listbox.insert(END, item)

    # Create a scrollbar
    scrollbar = ttk.Scrollbar(box_frame, orient="vertical", command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)

    # Pack the listbox and scrollbar
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Bind the item click event to a function
    listbox.bind('<<ListboxSelect>>', view_recipe_window)

items_box(window1)




window1.mainloop()