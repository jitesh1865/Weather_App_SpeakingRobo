from gtts import gTTS
from playsound import playsound
import requests
import json

import os

city=input("Enter a City Name by user : \n")

url= f"http://api.weatherapi.com/v1/current.json?key=91dbec122cfd492b88a172049242105&q={city}&aqi=yes"

r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
g=wdic["current"]["temp_c"]
h="Temperature of "+city +"at current position is "+ str(g) 
print(city)  #Print the name of city
print(g) # print temperature 
fh=gTTS(h,lang='en')
fh.save('weather.mp3')
playsound('weather.mp3')
os.remove('weather.mp3')  #everytime it is created new and remove earlier one