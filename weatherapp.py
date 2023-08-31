import tkinter as tk
import daytime as dt
import requests

class MyGUI:

  def __init__(self):
    self.window = tk.Tk()
    self.window.title("The Weather App")
    self.window.geometry("400x400")

    self.entered_city=tk.StringVar()

    self.label = tk.Label(self.window, text="Please enter a city to view the weather:", font=("arial", 12))
    self.label.pack()

    self.entered_city = tk.Text(self.window, height=5, font=("Arial", 18))
    self.entered_city.pack(padx=25, pady=25)

    self.button = tk.Button(self.window, text="Search", font=("Arial", 18), command=self.show_message)
    self.button.pack(padx=10, pady=10)

    self.window.mainloop()

  def show_message(self):
    print(self.entered_city.get)


MyGUI()

'''
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = open('api_key.txt', 'r').read()
city = input("E")

def kelvin_to_c_f(kelvin):
  celsius = int(kelvin - 273.15)
  fahrenheit = int(celsius * (9/5) + 32)
  return celsius, fahrenheit

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_c_f(temp_kelvin)
feels_like_kelvin = response ['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_c_f(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']

print(f'Current weather conditions in {city}: {description}.')
print(f'Current temperature in {city}: {temp_celsius:.2f}*C or {temp_fahrenheit}*F')

'''
tk.mainloop()