from tkinter import *
from tkinter import ttk, scrolledtext
import tkinter.messagebox
import pickle





##------------------------------------------------------------------
##------------------------------------------------------------------
class MainWindow:


    def __init__(self, window):
        self.window = window
        self.window.geometry(newGeometry="500x400+10+10")
        self.window.title("MY RECIPES")

        self.title_app = Label(self.window, text="Favourite Recipes",fg="white", bg="black", relief="solid", font=("arial",20,"bold"))
        self.title_app.pack(fill=BOTH, pady=10, padx=0, expand=False)

        self.items = [f"Item {i}" for i in range(1, 21)]

        self.recipe_name = None
        self.recipe_description = None

        self.menu_app()
        self.add_delete_button()
        self.list_box()


    def exit_app(self):
        exit()


    def about_app(self):
        tkinter.messagebox.showinfo("About", 'This is a custom-made app to save and view food recipes')


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
        add_button = Button(self.window,text="ADD", fg="green", bg="white",
                            relief=RIDGE, font=("arial",14,"bold"),
                            command=self.open_add_recipe_window)
        add_button.place(x=10, y=50)

        delete_button = Button(self.window,text="DELETE", fg="red", bg="white",
                               relief=RIDGE, font=("arial",14,"bold"))
        delete_button.place(x=100, y=50)


    def list_box(self):
        box_frame = Frame(self.window, width=50, height=20)
        box_frame.place(x=10, y=100)
        self.listbox = Listbox(box_frame, selectmode=SINGLE)

        for item in self.items:
            self.listbox.insert(END, item)
        scrollbar = ttk.Scrollbar(box_frame, orient="vertical",
                                  command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox.bind('<<ListboxSelect>>', self.open_view_recipe_window)


    def open_add_recipe_window(self):
        add_recipe_window = Toplevel(self.window)
        AddRecipeWindow(add_recipe_window, self.items)


    def open_view_recipe_window(self):
        view_recipe_window = Toplevel(self.window)
        ViewRecipeWindow(view_recipe_window)

    def run(self):
        self.window.mainloop()





##-------------------------------------------------------------------
##-------------------------------------------------------------------
class AddRecipeWindow:
    def __init__(self, window, items):
        self.window = window
        self.window.title("New Recipe")
        self.window.geometry("850x500")

        self.items = items

        recipe_name = Label(self.window, text="Recipe name",fg="black", font=("arial",12))
        recipe_name.place(x=10, y=20)

        steps = Label(self.window, text="Steps",fg="black", font=("arial",12))
        steps.place(x=10, y=100)

        recipe_name_entry = Entry(self.window)
        recipe_name_entry.place(x=150, y=20)

        self.recipe_name = recipe_name_entry.get()
        print(type(self.recipe_name))

        check_button = Button(self.window,text="Check", fg="Blue", font=("arial",12,"bold"),
                              command=self.check_redundancy)
        check_button.place(x=300, y=20)

        recipe_description_entry = scrolledtext.ScrolledText(self.window, wrap=WORD,
                                                             width=75, height=15)
        recipe_description_entry.place(x=150, y=100)

        self.large_text = recipe_description_entry.get("1.0", END)
        print(type(self.large_text))

        save_button = Button(self.window,text="Save", fg="green", bg="white", relief=RIDGE,
                             font=("arial",14,"bold"))
        save_button.place(x=100, y=400)

    def check_redundancy(self):

        if self.recipe_name in self.items:
            tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')






##-------------------------------------------------------------------
##-------------------------------------------------------------------
class ViewRecipeWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("REMEMBER")
        self.window.geometry("1000x500")
        label2 = Label(self.window, text="", relief= 'solid', font = ('arial', 12, 'bold')).place(x=10, y=50)
        close_button1 = Button(self.window,text="Close", fg="red", bg="white", relief=RIDGE, font=("arial",14,"bold"), command=self.exit_app)
        close_button1.place(x=200, y=200)
        save_button = Button(self.window,text="Save", fg="green", bg="white", relief=RIDGE, font=("arial",14,"bold"))
        save_button.place(x=10, y=400)


if __name__ == "__main__":
    window = Tk()
    app = MainWindow(window)
    app.run()

