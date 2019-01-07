'''
Web scraping national weather forecasts
San Francisco 
@author: Adams-Developer

'''

import requests
import itertools
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

print(tonight.prettify())
print("\n")

#Extracting information from page
#Forecast period - Tonight
#Short description of weather conditions
#The low temperature
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)
print("\n")

#Extract the title attribute from img tag
#Treat BeautifulShop obj like dictionary
#and pass in the attribute we want to use as a key
img = tonight.find("img")
desc = img['title']

print(desc)
print("\n")

#Extract everything
#Select all items with the class period-name
#inside an item with the class tombstone-container
#call get_text on each BeautifulSoup obj
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

['Tonight',
'Thursday',
'ThursdayNight',
'Friday',
'FridayNight',
'Saturday',
'SaturdayNight',
'Sunday',
'SundayNight']

#getting the other fields
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)
print("\n")
