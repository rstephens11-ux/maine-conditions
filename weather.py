import json
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=43.83&longitude=-69.68&current_weather=true&temperature_unit=fahrenheit"

with urllib.request.urlopen(url) as f:
    data = json.load(f)

temp = data["current_weather"]["temperature"]
print("It is", temp, "degrees F in Southport right now.")

