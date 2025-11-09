
import urllib.request
import json

API_KEY="df4adfb79b383da1a9e960736703b99e"
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"

response = urllib.request.urlopen(url)
data = json.loads(response.read())

print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])



