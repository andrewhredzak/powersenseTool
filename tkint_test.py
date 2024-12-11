import tkinter as tk
from tkinter import ttk  # For modern-looking widgets
import os

def button_clicked():
    label.config(text="Button clicked!")

# Create main window
root = tk.Tk()
root.title("My App with Icon")
root.geometry("300x500")  # Set initial size

# Set the icon (replace 'path/to/your/icon.ico' with the actual path)
icon_path = os.path.join(os.getcwd(), "powersenseTool", "nasa_logo_icon_170926.ico")
root.iconbitmap(icon_path)

# Create a label
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text="Click Me", command=button_clicked)
button.pack()

# Run the main loop
root.mainloop()