import tkinter as tk
import unittest
import os

class HelloGUI:
    """A simple Class to display a Hello World GUI."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hello World")
        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack(pady=20)

    def run(self):
        """Starts the tkinter main loop."""
        self.root.mainloop()

class TestHelloGUI(unittest.TestCase):
    """Unit tests to verify all aspects of the HelloGUI class."""
    
    def test_window_title(self):
        """Verify the window title is set correctly."""
        # Use a try-except here so the test doesn't crash in Codespaces
        try:
            app = HelloGUI()
            self.assertEqual(app.root.title(), "Hello World")
            app.root.destroy() # Close the window immediately
        except tk.TclError:
            self.skipTest("No display available in this environment")

    def test_label_text(self):
        """Verify the label displays the correct text."""
        try:
            app = HelloGUI()
            self.assertEqual(app.label["text"], "Hello, World!")
            app.root.destroy()
        except tk.TclError:
            self.skipTest("No display available in this environment")

if __name__ == "__main__":
    # 1. Run the tests automatically
    print("--- Running Automated Unit Tests ---")
    unittest.main(exit=False, buffer=True)
    
    # 2. Try to launch the GUI only if a screen exists
    if "DISPLAY" in os.environ or os.name == 'nt':
        print("\nLaunching Application...")
        gui = HelloGUI()
        gui.run()
    else:
        print("\nNote: GUI skipped because no screen (DISPLAY) was detected.")
        print("This is expected behavior in GitHub Codespaces.")a