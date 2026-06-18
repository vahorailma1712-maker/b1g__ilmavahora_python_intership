import requests

api_key = "d78485184cfd300422bce37e7ff44dca"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Error:", data.get("message", "Unable to fetch weather data"))