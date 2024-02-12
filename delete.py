import tkinter as tk
import tkinter.messagebox
import pickle
from file import EditFile

class DeleteRecipeWindow:


    def __init__(self, window, main_window):

        self.window = window
        self.main_window = main_window
        self.window.geometry("360x420")

        data = EditFile.read_from_file()

        items = sorted(list(data.keys()))


        self.box_frame = tk.Frame(self.window)
        self.box_frame.place(x=20, y=30, width=300, height=300)
        self.listbox = tk.Listbox(self.box_frame, selectmode=tk.SINGLE, font=("arial", 12))

        for item in items:
            self.listbox.insert(tk.END, item)
        scrollbar = tk.Scrollbar(self.box_frame, orient="vertical",
                                  command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        self.delete_button = tk.Button(window, text="Delete", command = self.delete_recipe)
        self.delete_button.place(x=250, y=350)


    def delete_recipe(self):

        index = self.listbox.curselection()
        selected_item = self.listbox.get(index)


        # Load existing data from the pickle file
        existing_data = EditFile.read_from_file()

        # Delete data from dictionary
        del existing_data[selected_item]

        # Write the updated data back to the pickle file
        EditFile.overwrite_file(existing_data)

        tkinter.messagebox.showinfo("Message", 'Recipe deleted from Database.')

        self.main_window.update_listbox(list(existing_data.keys()))
        self.update_listbox2(list(existing_data.keys()))


    def update_listbox2(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)

