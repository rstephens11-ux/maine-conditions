import json
import urllib.request

places = [
    {"name": "Southport", "lat": 43.83, "lon": -69.68},
    {"name": "Pemaquid Beach", "lat": 43.871, "lon": -69.519},
    {"name": "Popham Beach", "lat": 43.752, "lon": -69.784},
    {"name": "Greenville", "lat": 45.459, "lon": -69.591},
    {"name": "Mount Vernon", "lat": 40.923, "lon": -73.837},
    {"name": "Shrub Oak", "lat": 41.321, "lon": -73.830},
    {"name": "Sao Paulo", "lat": -23.534, "lon": -46.625},
    {"name": "Rio Preto", "lat": -20.813, "lon": -49.380},
    {"name": "Rondonopolis", "lat": -16.460, "lon": -54.640},
]

words = {
    0: "clear",
    1: "mostly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "foggy",
    51: "drizzly",
    53: "drizzly",
    55: "drizzly",
    61: "rainy",
    71: "snowy",
    80: "showery",
    95: "stormy",
}

rows = []

for place in places:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={place['lat']}&longitude={place['lon']}&current_weather=true&temperature_unit=fahrenheit"
    with urllib.request.urlopen(url) as f:
        data = json.load(f)

    temp = data["current_weather"]["temperature"]
    code = data["current_weather"]["weathercode"]
    sky = words.get(code, "unclear")

    line = f"{place['name']}: {temp} F and {sky}"
    print(line)
    rows.append(f"<p>{place['name']}: {temp}&deg;F and {sky}</p>")

html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Maine Conditions</title>
<style>
  body {{ font-family: -apple-system, sans-serif; max-width: 30rem; margin: 3rem auto; padding: 0 1rem; background: #101418; color: #e6e1d6; }}
  h1 {{ font-size: 1.25rem; }}
  p {{ font-size: 1.1rem; }}
</style>
</head>
<body>
<h1>Maine Conditions</h1>
{"".join(rows)}
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)

print("Wrote index.html — open it in a browser.")
