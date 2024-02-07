
"""current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "im.png")
img = Image.open(image_path)
tk_img = ImageTk.PhotoImage(img)
img_label = Label(window1, image=tk_img)
img_label.pack()"""

from tkinter import *
from tkinter import ttk, scrolledtext
import tkinter.messagebox
import pickle





class RecipeApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(newGeometry="500x400+10+10")
        self.window.title("MY RECIPES")

        self.title_app = Label(self.window, text="Favourite Recipes",fg="white", bg="black", relief="solid", font=("arial",20,"bold"))
        self.title_app.pack(fill=BOTH, pady=10, padx=0, expand=False)

        self.items = [f"Item {i}" for i in range(1, 21)]

        self.name = None
        self.large_text = None
        self.text_variable = StringVar()

        self.menu_app()
        self.add_delete_button()
        self.items_box()

    def exit_app(self):
        exit()

    def about_app(self):
        tkinter.messagebox.showinfo("About", 'This is a custom-made app to record and view food recipes')

    def menu_app(self):
        menu = Menu(self.window)
        self.window.config(menu=menu)

        subm1 = Menu(menu)
        menu.add_cascade(label="File", menu=subm1)
        subm1.add_command(label="Exit", command=self.exit_app)

        subm2 = Menu(menu)
        menu.add_cascade(label="Option", menu=subm2)
        subm2.add_command(label="About", command=self.about_app)

    def add_delete_button(self):
        add_button = Button(self.window,text="ADD", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=self.add_recipe_window)
        add_button.place(x=10, y=50)

        delete_button = Button(self.window,text="DELETE", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"))
        delete_button.place(x=100, y=50)

    def items_box(self):
        box_frame = Frame(self.window, width=50, height=20)
        box_frame.place(x=10, y=100)
        self.listbox = Listbox(box_frame, selectmode=SINGLE)

        for item in self.items:
            self.listbox.insert(END, item)
        scrollbar = ttk.Scrollbar(box_frame, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox.bind('<<ListboxSelect>>', self.view_recipe_window)


    def add_recipe_window(self):
        window3 = Toplevel(self.window)
        window3.title("New Recipe")
        window3.geometry("850x500")

        self.name = StringVar()

        recipe_name = Label(window3, text="Recipe name",fg="black", font=("arial",12))
        recipe_name.place(x=10, y=20)

        recipe_name_entry = Entry(window3,textvariable=self.name)
        recipe_name_entry.place(x=150, y=20)

        check_button = Button(window3,text="Check", fg="Blue", font=("arial",12,"bold"), command=self.check_redundancy)
        check_button.place(x=300, y=20)

        steps = Label(window3, text="Steps",fg="black", font=("arial",12))
        steps.place(x=10, y=100)

        large_text_entry = scrolledtext.ScrolledText(window3, wrap=WORD, width=75, height=15)
        large_text_entry.place(x=150, y=100)

        self.large_text = large_text_entry.get("1.0", END)
        print(self.large_text)

        save_button = Button(window3,text="Save", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=self.save_content)
        save_button.place(x=100, y=400)

    def check_redundancy(self):

        fn1 = self.name.get()
        print (fn1)
        if fn1 in self.items:
            tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')


    def view_recipe_window(self, event):

        window2 = Toplevel(self.window)
        window2.title("REMEMBER")
        window2.geometry("1000x500")
        label2 = Label(window2, text="", relief= 'solid', font = ('arial', 12, 'bold')).place(x=10, y=50)
        close_button1 = Button(window2,text="Close", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=self.exit_app)
        close_button1.place(x=200, y=200)
        save_button = Button(window2,text="Save", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"))
        save_button.place(x=10, y=400)

    def save_content(self):
        print(self.large_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = RecipeApp()
    app.run()


