Assignment 11:

Overview:

This project demonstrates the development of multiple object-oriented GUI applications using Python and Tkinter. The assignment includes several programs that showcase concepts such as event-driven programming, file handling, data structures, and API integration.

---
Programs Included:

Hello World GUI:

A simple Tkinter application that displays "Hello, World!" in a window.

Text Editor:

A fully functional GUI text editor with:

* File menu (New, Open, Save, Save As, Exit)
* Edit menu (Cut, Copy, Paste with keyboard shortcuts)
* Right-click context menu
* Help menu with About dialog

Paint App:

A basic drawing application that allows:

* Freehand drawing on a canvas
* Color selection
* Adjustable brush size

Crd Game:

An object-oriented card game implementation that includes:

* Deck and card handling using lists
* Player vs computer gameplay
* Score tracking using dictionaries

Weather Application:

A GUI-based weather app that:

* Fetches real-time weather data using the OpenWeatherMap API
* Displays temperature for a given city
* Demonstrates API usage and JSON handling

Serial Monitor:

A Python-based serial monitor that:

* Reads data from a serial port using pySerial
* Displays incoming data in real-time
* Designed for use with Arduino or similar devices

---

Requirements:

* Python 3.x
* Tkinter (included with Python)
* requests library
* pyserial library

Install dependencies:

```
pip install requests pyserial
```

---

How to run:

Navigate to the Assignment 11 folder:

```
cd Assignment11
```

Run any program:

```
python hello_world.py
python text_editor.py
python paint_app.py
python card_game.py
python weather_app.py
python serial_monitor.py
```

---
Notes:

* GUI applications (Tkinter) must be run locally and will not work in browser-based environments like GitHub Codespaces.
* The Serial Monitor requires a physical device and correct COM port configuration.
* Replace the API key in `weather_app.py` with your own from OpenWeatherMap.

---

Unit testing:
Unit tests are included to validate core components such as the card deck functionality.

Run tests using:

```
python test_card_game.py
```

---

What i learned:

In this assignment, I learned how to design and implement object-oriented GUI applications using Python and Tkinter. I gained hands-on experience with event-driven programming, file handling, and user interface design. I also learned how to integrate external APIs and work with real-time data, as well as how to communicate with hardware devices using serial communication.

Additionally, I improved my understanding of data structures such as lists and dictionaries by applying them to real-world applications like card games and weather tracking. I also learned the importance of debugging, testing, and organizing code using GitHub.

I plan to apply this knowledge in my future career by building interactive desktop applications and expanding into more advanced software development, including full-stack development and hardware-software integration.

---

Repository Structure:

```
Assignment11/
│
├── hello_world.py
├── text_editor.py
├── paint_app.py
├── card_game.py
├── weather_app.py
├── serial_monitor.py
├── test_card_game.py
└── README.md
```

---

Conclusion:

This project demonstrates a strong foundation in GUI programming, object-oriented design, and practical software development using Python.
