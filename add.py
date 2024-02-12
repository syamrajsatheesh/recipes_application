import tkinter as tk
import tkinter.messagebox
from file import EditFile

class AddRecipeWindow:


    def __init__(self, window, main_window):
        self.window = window
        self.main_window = main_window
        self.window.title("New Recipe")
        self.window.geometry("600x450")

        self.recipe_name = tk.Label(window, text="Recipe name")
        self.recipe_name.grid(row=1, column=0, padx=10, pady=10)

        self.recipe_name_entry = tk.Entry(window)
        self.recipe_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.check_button = tk.Button(self.window, text="Check", command=self.check_redundancy)
        self.check_button.grid(row=1, column=2, padx=1, pady=10)

        self.steps = tk.Label(window, text="Steps")
        self.steps.grid(row=2, column=0, padx=10, pady=10)

        self.steps_scroll = tk.Scrollbar(window)
        self.steps_scroll.grid(row=2, column=6, sticky="nsew")

        self.steps_box = tk.Text(window, height=20, width=50, wrap="word", yscrollcommand=self.steps_scroll.set)
        self.steps_box.grid(row=2, column=1, columnspan=5, padx=10, pady=10)
        self.steps_scroll.config(command=self.steps_box.yview)

        self.save_button = tk.Button(window, text="Save", command=self.save_data_to_dat)
        self.save_button.grid(row=3, column=4, columnspan=2, padx=10, pady=10)


    def check_redundancy(self):

        name = self.recipe_name_entry.get()
        if name in self.items:
            tkinter.messagebox.showinfo("Warning!", 'Recipe already exists in database.')
        else:
            tkinter.messagebox.showinfo("Warning", "Recipe not  in the database")


    def save_data_to_dat(self):

        flag = False

        key = self.recipe_name_entry.get()
        value = self.steps_box.get("1.0", tk.END)

        if key == None or key == "" or value == None or value == "":
            if key == None or key == "":
                tkinter.messagebox.showinfo("Warning!", 'Write the Recipe Name.')
            if value == None or value == "":
                tkinter.messagebox.showinfo("Warning!", 'Write the Steps.')
            
        else:
            existing_data = EditFile.write_to_file(key, value)

            self.main_window.update_listbox(list(existing_data.keys()))
            self.window.destroy()
