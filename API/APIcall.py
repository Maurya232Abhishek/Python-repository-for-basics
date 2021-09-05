import requests
import json
import datetime as dt
appid="4a1f8a61b74546825af1e0be106e797b"
city="varanasi"
url="https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(city,appid)
response=requests.get(url)
code= response.status_code
print(code)
jsondata=json.loads(response.text)
print(jsondata)

#print(jsondata['weather'][0]["main"])
#print(jsondata["main"]["temp"])