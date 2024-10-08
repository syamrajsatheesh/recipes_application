import tkinter as tk

class ViewRecipeWindow:
    def __init__(self, window, recipe_name):
        self.window = window
        self.window.title(recipe_name)
        self.window.geometry("600x450")

        self.scrollbar = tk.Scrollbar(window)
        self.scrollbar.place(x=20, y=120)

        self.text_box = tk.Text(window, wrap="word", yscrollcommand=self.scrollbar.set)
        self.text_box.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_box.yview)

    def display_item(self, item):
        self.text_box.insert(tk.END, item + "\n")

