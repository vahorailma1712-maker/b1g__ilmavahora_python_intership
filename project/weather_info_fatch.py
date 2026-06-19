import requests


API_KEY = 'd78485184cfd300422bce37e7ff44dca api key'
BASE_URL = "url:https://home.openweathermap.org"


city = input('input the city name:')
print(city)

#city = ('enter the city')

print('Displaing weather report for: '+ city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text);
