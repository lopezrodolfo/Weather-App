import os

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_weather(api_key, city):
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric",
            timeout=10,
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature_celsius = weather_data["main"]["temp"]
        temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
        weather_description = weather_data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature_fahrenheit}°F")
        print(f"Description: {weather_description}")
    else:
        print("Failed to retrieve weather data")


def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return
    city = input("Enter city name: ")
    weather_data = fetch_weather(api_key, city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
