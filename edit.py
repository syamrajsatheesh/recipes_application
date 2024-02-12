import tkinter as tk
from file import EditFile
import tkinter.messagebox

class EditRecipeWindow:
    def __init__(self, window, main_window):
        self.window = window
        self.main_window = main_window
        self.window.geometry("800x450")
        self.data = EditFile.read_from_file()
        self.key = None

        self.recipes_listbox = tk.Listbox(window, width=20)
        self.recipes_listbox.place(x=20, y=30, width=180, height=400)
        self.recipes_listbox.bind("<<ListboxSelect>>", self.on_key_select)

        self.title_label = tk.Label(window, text="Recipe Name:")
        self.title_label.place(x=240, y=30)

        self.recipe_title = tk.Entry(window)
        self.recipe_title.place(x=330, y=30, width=410, height=20)

        self.recipe_description = tk.Text(window, wrap="word")
        self.recipe_description.place(x=240, y=80, width=500, height=300)

        self.save_button = tk.Button(window, text="Save", command=self.save_value)
        self.save_button.place(x=700, y=400)

        self.list_scrollbar = tk.Scrollbar(self.recipes_listbox, command=self.recipes_listbox.yview)
        self.list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.recipes_listbox.config(yscrollcommand=self.list_scrollbar.set)


        self.load_keys()

    def load_keys(self):
        for key in sorted(self.data.keys()):
            self.recipes_listbox.insert(tk.END, key)

    def on_key_select(self, event):
        selected_index = self.recipes_listbox.curselection()
        if selected_index:
            self.key = self.recipes_listbox.get(selected_index)
            value = self.data[self.key]
            ##self.recipe_title.config(text=key)
            self.recipe_title.delete(0, tk.END)
            self.recipe_title.insert(tk.END, self.key)
            self.recipe_description.delete(1.0, tk.END)
            self.recipe_description.insert(tk.END, value)

    def save_value(self):


        new_name = self.recipe_title.get()
        new_description = self.recipe_description.get(1.0, tk.END)

        if new_name == None or new_name == "":
            tkinter.messagebox.showinfo("Message", 'Recipe name box is empty.')

        else:

            del self.data[self.key]
            self.data[new_name] = new_description
            EditFile.overwrite_file(self.data)
            tkinter.messagebox.showinfo("Message", 'Recipe Edited.')

        self.main_window.update_listbox(list(self.data.keys()))
        self.update_listbox3(sorted(list(self.data.keys())))


    def update_listbox3(self, items):
        self.recipes_listbox.delete(0, tk.END)
        for item in items:
            self.recipes_listbox.insert(tk.END, item)




