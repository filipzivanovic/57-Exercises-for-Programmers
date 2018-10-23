import requests
import json


def find_city(input_city, input_country, cities):
    for city in cities:
        if input_city == city["name"] and input_country == city["country"]:
            return city["id"]


winds = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]

with open("48_cities.json", "r") as file:
    cities = json.load(file)

while True:
    input_city = input("City: ")
    input_country = input("Country (abbr): ")
    city_id = find_city(input_city, input_country, cities)
    if not city_id:
        print("There is no such city. Try again:")
        continue
    break

url = "http://api.openweathermap.org/data/2.5/forecast?id=%s&appid=173eaed14777ce75653cc20ebdac21d0" % city_id
response = requests.get(url)
data = response.json()

weather = data["list"][0]["weather"][0]["main"]
temperature = data["list"][0]["main"]["temp"] - 273.15
wind = winds[round(int((data["list"][0]["wind"]["deg"] % 360) / 22.5), 0) + 1]

print("Weather: %s" % weather)
print("Temperature is : %d°C" % temperature)
print("Wind is : %s" % wind)
