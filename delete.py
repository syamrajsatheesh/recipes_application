import tkinter as tk
import tkinter.messagebox
import pickle
from file import EditFile

class DeleteRecipeWindow:


    def __init__(self, window, main_window):

        self.window = window
        self.main_window = main_window
        self.window.geometry("300x300")

        data = EditFile.read_from_file()

        items = sorted(list(data.keys()))


        self.box_frame = tk.Frame(self.window, width=80, height=60)
        self.box_frame.grid(row=1, column=1,rowspan=2,columnspan=2)
        self.listbox = tk.Listbox(self.box_frame, selectmode=tk.SINGLE)

        for item in items:
            self.listbox.insert(tk.END, item)
        scrollbar = tk.Scrollbar(self.box_frame, orient="vertical",
                                  command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        self.delete_button = tk.Button(window, text="Delete", command = self.view_recipe)
        self.delete_button.grid(row=2, column=3)


    def view_recipe(self):

        index = self.listbox.curselection()
        selected_item = self.listbox.get(index)


        # Load existing data from the pickle file
        with open("database.dat", 'rb') as file:
            existing_data = pickle.load(file)

        # Delete data from dictionary
        del existing_data[selected_item]

        # Write the updated data back to the pickle file
        with open("database.dat", 'wb') as file:
            pickle.dump(existing_data, file)

        tkinter.messagebox.showinfo("Message", 'Recipe deleted from Database.')

        self.main_window.update_listbox(list(existing_data.keys()))
        self.update_listbox2(list(existing_data.keys()))


    def update_listbox2(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)

