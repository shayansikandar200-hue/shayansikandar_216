import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"  # replace this

def get_weather():
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    data = requests.get(url).json()
    
    if data.get("main"):
        temp = data["main"]["temp"]
        label.config(text=f"{city}: {temp}°C")
    else:
        label.config(text="City not found")

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()