import tkinter as tk
import tkinter.messagebox
from add import AddRecipeWindow
from view import ViewRecipeWindow
from delete import DeleteRecipeWindow
from edit import EditRecipeWindow
from file import EditFile

class MainWindow:


    def __init__(self, window):
        self.window = window
        self.window.geometry(newGeometry="400x400+10+10")
        self.window.title("MY RECIPES")

        self.title_app = tk.Label(self.window, text="Favourite Recipes",fg="white",
                               bg="black", relief="solid", font=("arial",16,"bold"))
        self.title_app.pack(fill=tk.BOTH, pady=20, padx=0, expand=False)


        self.menu_app()
        self.add_edit_delete()
        self.listbox_app()


    def listbox_app(self):

        data = EditFile.read_from_file()

        items = sorted(list(data.keys()))

        self.box_frame = tk.Frame(self.window)
        self.box_frame.place(x=20, y=120, width=300, height=200)
        self.listbox = tk.Listbox(self.box_frame, selectmode=tk.SINGLE, font=("arial", 12))

        for item in items:
            self.listbox.insert(tk.END, item)
        scrollbar = tk.Scrollbar(self.box_frame, orient="vertical",
                                  command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.bind('<<ListboxSelect>>', self.open_view_recipe_window)
    



    def update_listbox(self, items):
        self.listbox.delete(0, tk.END)
        for item in sorted(items):
            self.listbox.insert(tk.END, item)


    def exit_app(self):
        exit()


    def about_app(self):
        tkinter.messagebox.showinfo("About", 'This is a custom-made app to save and view food recipes')


    def menu_app(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        subm1 = tk.Menu(menu)
        menu.add_cascade(label="File", menu=subm1)
        subm1.add_command(label="Exit", command=self.exit_app)

        subm2 = tk.Menu(menu)
        menu.add_cascade(label="Option", menu=subm2)
        subm2.add_command(label="About", command=self.about_app)


    def add_edit_delete(self):
        add_button = tk.Button(self.window,text="ADD", fg="green", bg="white",
                            relief=tk.RIDGE, font=("arial",12,"bold"),
                            command=self.open_add_recipe_window)
        add_button.place(x=20, y=70)

        edit_button = tk.Button(self.window,text="EDIT", fg="blue", bg="white",
                               relief=tk.RIDGE, font=("arial",12,"bold"),
                               command=self.open_edit_recipe_window)
        edit_button.place(x=100, y=70)

        delete_button = tk.Button(self.window,text="DELETE", fg="red", bg="white",
                               relief=tk.RIDGE, font=("arial",12,"bold"),
                               command=self.open_delete_recipe_window)
        delete_button.place(x=180, y=70)



    def open_add_recipe_window(self):
        add_recipe_window = tk.Toplevel(self.window)
        add_recipe = AddRecipeWindow(add_recipe_window, self)


    def open_view_recipe_window(self, event):

        index = self.listbox.curselection()
        selected_item = self.listbox.get(index)
        ##item_description = self.load_data_from_dat(selected_item)

        item_description = EditFile.read_from_file()[selected_item]

        open_view_recipe_window_window = tk.Toplevel(self.window)
        item_viewer = ViewRecipeWindow(open_view_recipe_window_window, selected_item)
        item_viewer.display_item(item_description)

    def open_delete_recipe_window(self):

        delete_recipe_window = tk.Toplevel(self.window)
        delete_recipe = DeleteRecipeWindow(delete_recipe_window, self)



    def open_edit_recipe_window(self):

        edit_recipe_window = tk.Toplevel(self.window)
        edit_recipe = EditRecipeWindow(edit_recipe_window, self)