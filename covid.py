import tkinter as tk
from datetime import datetime

import requests
import datetime

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data["cases"])
    total_deaths = str(json_data["deaths"])
    today_cases = str(json_data["todayCases"])
    today_deaths = str(json_data["todayDeaths"])
    today_recovered = str(json_data["todayRecovered"])
    updated_at = json_data['updated']
    date: datetime = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text = "Total Cases: "+total_cases+
    "\nTotal Deaths: " + total_deaths+
    "\nToday Cases: "+today_cases+
    "\nToday Cases: "+today_deaths+
    "\nToday Recovered: "+today_recovered)
    label2.config(text = date)

parent = tk.Tk()
parent.geometry("600x400")
parent.title("Covid-19 Tracker App")
f = ("Helvetica", 15, "bold")
button = tk.Button(parent, font = f , text = "Click here to get Covid details", command = getCovidData)
button.pack(pady = 20)
label = tk.Label(parent , font = f)
label.pack(pady = 20)
label2 = tk.Label(parent , font = 6)
label2.pack()
parent.mainloop()
