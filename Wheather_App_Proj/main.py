import requests                 # youcan bring things through network
import  json
import win32com.client  as wincom     # to speak text

# your api key is
# https://api.weatherapi.com/v1/current.json?key=c9d44c619550424f82c153454232011&q=delhi

city = input("Enter Your Name of City : \n ")

url= f"https://api.weatherapi.com/v1/current.json?key=c9d44c619550424f82c153454232011&q={city}"

r=requests.get(url)

# print(r.text)                              # our output interm of dictionary we have to separate it in dictionary parts
                                            # by uisng jason

weather_dic = json.loads(r.text)

# print(weather_dic)
current_temp =weather_dic['current']['temp_c']

# print(f"current tempreture of {city} city is :{current_temp} d/c ")
speaker = wincom.Dispatch("SAPI.SpVoice")

text= f"current tempreture of {city} city is :{current_temp}  degrees "

speaker.Speak(text)
