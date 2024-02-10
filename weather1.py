import tkinter as tk
import requests
import time 
Api= 'd01394afe15b6d7f6a57694cf32e67c1'
def Weather_Report(format):

    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+f"&appid="+Api
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

    first = condition + "\n" + str(temp) +  u"\u00b0" +"C"
    second = "\n" + "Max Temp: " + str(max_temp) +  u"\u00b0" +"C"+ "\n" + "Min temp: " + str(min_temp)+  u"\u00b0" +"C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: "+ str(humidity)+" %" + "\n" + "Wind Speed: "+str(wind)+" Km/hr"  +"\n"+ "Sunrise: " + str(sunrise)+"\n" +"Sunset: "+str(sunset)
    label1.config(text = first)
    label2.config(text = second)


format = tk.Tk()
format.geometry("600x500")
format.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

label3 = tk.Label(format,text="Enter city name",font=t)
label3.pack()

textfield = tk.Entry(format,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',Weather_Report)

label1 = tk.Label(format, font= t)
label1.pack()
label2 = tk.Label(format, font =f)
label2.pack()

format.mainloop()
