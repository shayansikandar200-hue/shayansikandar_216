"""
Raster Graphics Editor (Simple Paint)
"""

import tkinter as tk
import unittest


class PaintProgram:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Paint")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.color = "black"
        self.size = 5

    def paint(self, event):

        x = event.x
        y = event.y

        self.canvas.create_oval(
            x,
            y,
            x + self.size,
            y + self.size,
            fill=self.color,
            outline=self.color
        )

    def run(self):
        self.root.mainloop()


class TestPaintProgram(unittest.TestCase):

    def test_default_color(self):
        app = PaintProgram()
        self.assertEqual(app.color, "black")

    def test_brush_size(self):
        app = PaintProgram()
        self.assertEqual(app.size, 5)


if __name__ == "__main__":
    unittest.main()