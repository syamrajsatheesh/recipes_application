import tkinter as tk
from tkinter import ttk

def create_window_with_listbox():
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Window with Listbox Example")
    root.geometry("500x500")

    # Create a box (Frame) inside the window
    box_frame = tk.Frame(root, padx=20, pady=20)
    box_frame.pack()

    # Create a list of items
    items = [f"Item {i}" for i in range(1, 21)]

    # Create a Tkinter listbox inside the box_frame
    listbox = tk.Listbox(box_frame, selectmode=tk.SINGLE)
    
    # Insert items into the listbox
    for item in items:
        listbox.insert(tk.END, item)

    # Create a scrollbar for the listbox
    scrollbar = ttk.Scrollbar(box_frame, orient="vertical", command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)

    # Pack the listbox and scrollbar
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to create the window with a listbox
create_window_with_listbox()
