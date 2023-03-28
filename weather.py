import requests

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data["main"]["temp"]

    print("weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occured.")