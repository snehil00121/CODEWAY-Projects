import tkinter as tk
import requests
import time 
# d01394afe15b6d7f6a57694cf32e67c1
def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d01394afe15b6d7f6a57694cf32e67c1"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.25)
    min_temp = int(json_data['main']['temp'] - 273.25)
    max_temp = int(json_data['main']['temp'] - 273.25)
    pressure = json_data['main']['pressure']
    humidity =json_data['main']['humidity']
    wind =json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: "+ str(humidity) + "\n" + "Wind Speed: "+str(wind)  + "Sunrise: " + str(sunrise) +"Sunset: "+str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas, font= t)
label1.pack()
label2 = tk.Label(canvas, font =f)
label2.pack()

canvas.mainloop()