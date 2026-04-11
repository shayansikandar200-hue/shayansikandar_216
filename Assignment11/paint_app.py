import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        root.title("Paint App")

        self.color = "black"
        self.brush = 5

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.draw)

        tk.Button(root, text="Color", command=self.pick_color).pack()

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill=self.color, outline=self.color)

    def pick_color(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.color = c

if __name__ == "__main__":
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()