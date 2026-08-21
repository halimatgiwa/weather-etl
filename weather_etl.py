import requests
import pandas as pd
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

cities = ["Lagos", "London", "New York"]

url = "https://api.openweathermap.org/data/2.5/weather"

weather_data = []

for city in cities:

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        weather_data.append({
            "City": data["name"],
            "Temperature_C": data["main"]["temp"],
            "Humidity_%": data["main"]["humidity"],
            "Weather_Condition": data["weather"][0]["main"],
            "Wind_Speed_mps": data["wind"]["speed"],
            "Date_Time": pd.to_datetime(data["dt"], unit="s")
        })

    else:
        print(f"Failed to retrieve weather data for {city}")
        print(response.json())

df = pd.DataFrame(weather_data)

print("\nCleaned Weather Dataset:")
print(df)

df.to_csv("weather_data.csv", index=False)

print("\nWeather data successfully saved to weather_data.csv")

print("\n--- BASIC WEATHER ANALYSIS ---")

highest_temp = df.loc[df["Temperature_C"].idxmax()]
highest_humidity = df.loc[df["Humidity_%"].idxmax()]
highest_wind = df.loc[df["Wind_Speed_mps"].idxmax()]

print(f"Highest temperature: {highest_temp['City']} ({highest_temp['Temperature_C']}°C)")
print(f"Highest humidity: {highest_humidity['City']} ({highest_humidity['Humidity_%']}%)")
print(f"Highest wind speed: {highest_wind['City']} ({highest_wind['Wind_Speed_mps']} m/s)")

print("\nWeather conditions by city:")
print(df[["City", "Weather_Condition"]])