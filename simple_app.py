import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Information", "Button clicked!")

def main():
    # Membuat jendela utama
    root = tk.Tk()
    root.title("Simple Tkinter App")

    # Membuat label
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=10)

    # Membuat tombol
    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=10)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()