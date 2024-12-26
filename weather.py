import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()  
    api_key = "d47069af4e848fedf0469538055581d9"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

       
        result_label.config(
            text=f"🌆 Weather in {city_name}:\n🌡️ Temperature: {temperature}°C\n☁️ Description: {weather_description.capitalize()}"
        )
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while fetching the weather data:\n{e}")
    except KeyError:
        messagebox.showerror("Error", "City not found. Please check the city name.")


root = tk.Tk()
root.title("Weather App 🌤️")
root.geometry("400x300")


title_label = tk.Label(root, text="Weather App 🌤️", font=("Arial", 18))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)


search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)


root.mainloop()
