"""
Simple Text Editor
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import unittest


class TextEditor:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Text Editor")

        self.text = tk.Text(self.root)
        self.text.pack(expand=True, fill="both")

        self.create_menu()

    def create_menu(self):

        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))

        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.about)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        menu.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path) as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, f.read())

    def save_file(self):
        path = filedialog.asksaveasfilename()
        if path:
            with open(path, "w") as f:
                f.write(self.text.get(1.0, tk.END))

    def about(self):
        messagebox.showinfo("About", "Simple Text Editor")

    def run(self):
        self.root.mainloop()


class TestTextEditor(unittest.TestCase):

    def test_new_file(self):
        editor = TextEditor()
        editor.text.insert("1.0", "test")
        editor.new_file()
        self.assertEqual(editor.text.get("1.0", "end-1c"), "")


if __name__ == "__main__":
    unittest.main()