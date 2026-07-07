import requests
import json

api_key = "3dd4cdcbd493d840c4208b2469efe0b6" 

print("Weather App")
print("-----------")

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    # 200 means successful request
    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nWeather Report")
        print("----------------")
        print("City:", city.title())
        print("Temperature:", temp, "°C")
        print("Weather:", weather.title())
        print("Humidity:", humidity, "%")

    # 401 means unauthorized (bad API key or key not yet active)
    elif response.status_code == 401:
        print("\n[Error] Invalid API Key. Please verify your OpenWeatherMap key or wait for it to activate.")

    # 404 means the city actually doesn't exist in their database
    elif response.status_code == 404:
        print("\n[Error] City not found. Please enter a valid city name.")

    # Catch-all for any other API errors (like rate limits)
    else:
        print(f"\n[Error] Failed with status code: {response.status_code}")

except Exception as e:
    print("\nSomething went wrong. Please check your internet connection.")