import tkinter as tk
import tkinter.messagebox
import pickle





##------------------------------------------------------------------
##------------------------------------------------------------------
class MainWindow:


    def __init__(self, window):
        self.window = window
        self.window.geometry(newGeometry="500x400+10+10")
        self.window.title("MY RECIPES")

        self.title_app = tk.Label(self.window, text="Favourite Recipes",fg="white",
                               bg="black", relief="solid", font=("arial",16,"bold"))
        self.title_app.pack(fill=tk.BOTH, pady=20, padx=0, expand=False)

        self.go_button = tk.Button(window, text="Go", command=self.open_add_recipe_window)
        self.go_button.place(x=300, y=300)

        self.menu_app()
        self.add_delete_button()

        file_path = "database.dat"

        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
            items = list(data.keys())
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

        self.box_frame = tk.Frame(self.window, width=80, height=60)
        self.box_frame.place(x=20, y=120)
        self.listbox = tk.Listbox(self.box_frame, selectmode=tk.SINGLE)

        for item in items:
            self.listbox.insert(tk.END, item)
        scrollbar = tk.Scrollbar(self.box_frame, orient="vertical",
                                  command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.bind('<<ListboxSelect>>', self.open_view_recipe_window)


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


    def add_delete_button(self):
        add_button = tk.Button(self.window,text="ADD", fg="green", bg="white",
                            relief=tk.RIDGE, font=("arial",12,"bold"),
                            )
        add_button.place(x=20, y=70)

        delete_button = tk.Button(self.window,text="DELETE", fg="red", bg="white",
                               relief=tk.RIDGE, font=("arial",12,"bold"))
        delete_button.place(x=100, y=70)



    def open_add_recipe_window(self):
        add_recipe_window = tk.Toplevel(self.window)
        essay_app = AddRecipeWindow(add_recipe_window)


    def open_view_recipe_window(self, event):

        index = self.listbox.curselection()
        selected_item = self.listbox.get(index)
        item_description = self.load_data_from_dat(selected_item)

        view_recipe_window = tk.Toplevel(self.window)
        item_viewer = ViewRecipeWindow(view_recipe_window)
        item_viewer.display_item(item_description)


    def load_data_from_dat(self, key):

        file_path = "database.dat"
        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)

            return data[key]
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None


class ViewRecipeWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Recipe Viewer")

        self.scrollbar = tk.Scrollbar(window)
        self.scrollbar.place(x=20, y=120)

        self.text_box = tk.Text(window, wrap="word", yscrollcommand=self.scrollbar.set)
        self.text_box.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_box.yview)

    def display_item(self, item):
        self.text_box.insert(tk.END, item + "\n")






##------------------------------------------------------------------
##------------------------------------------------------------------
class AddRecipeWindow:


    def __init__(self, window):
        self.window = window
        self.window.title("New Recipe")
        self.window.geometry("850x500")

        ## remove
        self.items = [f"Item {i}" for i in range(1, 21)]

        self.recipe_name = tk.Label(window, text="Recipe name")
        self.recipe_name.grid(row=0, column=0, padx=10, pady=10)

        self.recipe_name_entry = tk.Entry(window)
        self.recipe_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.check_button = tk.Button(self.window, text="Check", command=self.check_redundancy)
        self.check_button.grid(row=0, column=2, padx=1, pady=10)

        self.steps = tk.Label(window, text="Steps")
        self.steps.grid(row=1, column=0, padx=10, pady=10)

        self.steps_scroll = tk.Scrollbar(window)
        self.steps_scroll.grid(row=1, column=6, sticky="nsew")

        self.steps_box = tk.Text(window, height=20, width=50, wrap="word", yscrollcommand=self.steps_scroll.set)
        self.steps_box.grid(row=1, column=1, columnspan=5, padx=10, pady=10)
        self.steps_scroll.config(command=self.steps_box.yview)

        self.save_button = tk.Button(window, text="Save", command=self.save_data_to_dat)
        self.save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


        self.view_button = tk.Button(window, text="View", command=self.load_data_from_dat)
        self.view_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


    def check_redundancy(self):

        name = self.recipe_name_entry.get()
        if name in self.items:
            tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')
        else:
            tkinter.messagebox.showinfo("Warning", "Recipe not  in the database")


    """def save_content(self):
        essay_title = self.recipe_name_entry.get()
        essay_content = self.steps_box.get("1.0", tk.END)
        print("Recipe Name:", essay_title)
        print("Recipe Steps:")
        print(essay_content)"""


    def save_data_to_dat(self):

        key = self.recipe_name_entry.get()
        value = self.steps_box.get("1.0", tk.END)

        try:
            # Load existing data from the pickle file
            with open("database.dat", 'rb') as file:
                existing_data = pickle.load(file)
        except (FileNotFoundError, EOFError):
            # Handle the case where the file is not found or is empty
            existing_data = {}

        # Append new data to the existing data
        existing_data[key] = value

        # Write the updated data back to the pickle file
        with open("database.dat", 'wb') as file:
            pickle.dump(existing_data, file)



def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
