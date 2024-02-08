import tkinter as tk

root = tk.Tk()
root.title("Image Display")

# Load the image from the current directory
try:
    image = tk.PhotoImage(file="image.png")
    resized_image = image.subsample(5, 5)
    label = tk.Label(root, image=resized_image)
    label.pack()
except tk.TclError:
    print("Error: Image file not found or not supported.")

root.mainloop()
