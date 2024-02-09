import tkinter as tk
import tkinter.messagebox
import pickle

class DeleteRecipeWindow:


    def __init__(self, window):


        self.window = window
        self.window.geometry("500x500")
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


        self.delete_button = tk.Button(window, text="Delete", command = self.view_recipe)
        self.delete_button.place(x=300, y=300)


    def view_recipe(self):

        index = self.listbox.curselection()
        selected_item = self.listbox.get(index)

        tkinter.messagebox.showinfo("Message", 'Recipe deleted from Database.')


        # Load existing data from the pickle file
        with open("database.dat", 'rb') as file:
            existing_data = pickle.load(file)

        # Delete data from dictionary
        del existing_data[selected_item]

        # Write the updated data back to the pickle file
        with open("database.dat", 'wb') as file:
            pickle.dump(existing_data, file)

