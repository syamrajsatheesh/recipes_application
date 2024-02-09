import tkinter as tk

root = tk.Tk()
root.title("Scrollable List Box Example")
root.geometry("600x400")  # Set the size of the root window

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a list box
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, width=50, height=20)  # Increase the size of the list box
for i in range(1000):  # Adding 1000 items to the list box
    listbox.insert(tk.END, f"Item {i+1}")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Adjust the fill and expand options

# Configure the scrollbar to scroll the list box
scrollbar.config(command=listbox.yview)

root.mainloop()
