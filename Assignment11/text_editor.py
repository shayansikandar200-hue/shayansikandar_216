import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.file = None

        self.text = tk.Text(root, undo=True)
        self.text.pack(fill="both", expand=True)

        self.create_menu()
        self.create_context_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)

        # FILE
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu.add_cascade(label="File", menu=file_menu)

        # EDIT
        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))
        menu.add_cascade(label="Edit", menu=edit_menu)

        # HELP
        help_menu = tk.Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu)

        # Shortcuts
        self.root.bind("<Control-x>", lambda e: self.text.event_generate("<<Cut>>"))
        self.root.bind("<Control-c>", lambda e: self.text.event_generate("<<Copy>>"))
        self.root.bind("<Control-v>", lambda e: self.text.event_generate("<<Paste>>"))

    def create_context_menu(self):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))

        def show(event):
            menu.tk_popup(event.x_root, event.y_root)

        self.text.bind("<Button-3>", show)

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.file = None

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r") as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, f.read())
            self.file = path

    def save_file(self):
        if self.file:
            with open(self.file, "w") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename()
        if path:
            with open(path, "w") as f:
                f.write(self.text.get(1.0, tk.END))
            self.file = path

    def about(self):
        messagebox.showinfo("About", "Simple Text Editor\nTkinter GUI App")

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()