import requests
import tkinter

api_key = '30d4741c779ba94c470ca1f63045390a'
user_input = input("Enter city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404' or weather_data == '':
    print("No City found")
else:

    #print(weather_data.json())
    weather = weather_data.json()['weather'][0]['main']
    temp  = round((weather_data.json()['main']['temp'] - 32) *5/9)
    print(f'Weather in {user_input} is: {weather} and temperature is: {temp} deg')