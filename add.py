import tkinter as tk
import tkinter.messagebox
from file import EditFile

class AddRecipeWindow:


    def __init__(self, window, main_window):
        self.window = window
        self.main_window = main_window
        self.window.title("New Recipe")
        self.window.geometry("600x500")

        self.data = None

        self.recipe_name = tk.Label(window, text="Recipe name")
        self.recipe_name.place(x=20, y=20)

        self.recipe_name_entry = tk.Entry(window)
        self.recipe_name_entry.place(x=100, y=20, width =380)

        self.check_button = tk.Button(self.window, text="Check", command=self.check_redundancy)
        self.check_button.place(x=520, y=15)

        self.steps = tk.Label(window, text="Steps")
        self.steps.place(x=20, y=50)

        self.steps_box = tk.Text(window, height=20, width=50, wrap="word")
        self.steps_box.place(x=100, y=60, width=380, height=400)

        self.steps_scrollbar = tk.Scrollbar(self.steps_box, command=self.steps_box.yview)
        self.steps_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.steps_box.config(yscrollcommand=self.steps_scrollbar.set)


        self.save_button = tk.Button(window, text="Save", command=self.save_data_to_dat)
        self.save_button.place(x=520, y=440)


    def check_redundancy(self):

        self.data = EditFile.read_from_file()

        name = self.recipe_name_entry.get()
        if name.lower() in [x.lower() for x in list(self.data.keys())]:
            tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')
        else:
            tkinter.messagebox.showinfo("Warning", "Recipe not  in the database")


    def save_data_to_dat(self):


        key = self.recipe_name_entry.get()
        value = self.steps_box.get("1.0", tk.END)

        if key == None or key == "" or value == None or value == "":
            if key == None or key == "":
                tkinter.messagebox.showinfo("Warning!", 'Write the Recipe Name.')
            if value == None or value == "":
                tkinter.messagebox.showinfo("Warning!", 'Write the Steps.')
            
        else:
            existing_data = EditFile.write_to_file(key.title(), value)

            self.main_window.update_listbox(list(existing_data.keys()))
            self.window.destroy()
