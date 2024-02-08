import tkinter as tk

class DataEntryWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Enter Data")

        self.first_name_label = tk.Label(self.master, text="First Name:")
        self.first_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.last_name_label = tk.Label(self.master, text="Last Name:")
        self.last_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry = tk.Entry(self.master)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.age_label = tk.Label(self.master, text="Age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()

        display_window = tk.Toplevel(self.master)
        display_window.title("Entered Data")
        tk.Label(display_window, text="First Name: " + first_name).pack()
        tk.Label(display_window, text="Last Name: " + last_name).pack()
        tk.Label(display_window, text="Age: " + age).pack()

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        self.go_button = tk.Button(self.master, text="Go", command=self.open_data_entry_window)
        self.go_button.pack(pady=20)

    def open_data_entry_window(self):
        data_entry_window = tk.Toplevel(self.master)
        DataEntryWindow(data_entry_window)

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
