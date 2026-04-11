import tkinter as tk

class HelloWorldApp:
    def __init__(self, root):
        root.title("Hello World")
        tk.Label(root, text="Hello, World!", font=("Arial", 24)).pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    HelloWorldApp(root)
    root.mainloop()