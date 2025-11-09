import urllib.request
import json

API_KEY = "d2142ee9304d49beb10a8ca89871ac55"

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + API_KEY

response = urllib.request.urlopen(url)
data = json.loads(response.read())

articles = data["articles"]

print("Top 5 News Headlines:\n")

for i in range(5):
    print(str(i+1) + ".", articles[i]["title"])