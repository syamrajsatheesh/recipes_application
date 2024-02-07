import tkinter as tk
from tkinter import scrolledtext

class LargeTextBoxApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Large Text Entry")

        self.large_text_entry = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=40, height=10)
        self.large_text_entry.pack(padx=10, pady=10)

        self.display_button = tk.Button(self.window, text="Display Text", command=self.display_text)
        self.display_button.pack(pady=5)

        self.window.mainloop()

    def display_text(self):
        text = self.large_text_entry.get("1.0", tk.END)

        display_window = tk.Toplevel(self.window)
        display_window.title("Display Window")

        large_text_box = scrolledtext.ScrolledText(display_window, wrap=tk.WORD, width=60, height=20)
        large_text_box.pack(padx=10, pady=10)

        large_text_box.insert(tk.END, text)

if __name__ == "__main__":
    app = LargeTextBoxApp()
