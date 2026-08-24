import requests

import pandas as pd



API\_KEY = "YOUR\_API\_KEY"



cities = \["Lagos", "London", "New York"]



url = "https://api.openweathermap.org/data/2.5/weather"



weather\_data = \[]



for city in cities:



&#x20;   params = {

&#x20;       "q": city,

&#x20;       "appid": API\_KEY,

&#x20;       "units": "metric"

&#x20;   }



&#x20;   response = requests.get(url, params=params)



&#x20;   if response.status\_code == 200:

&#x20;       data = response.json()



&#x20;       weather\_data.append({

&#x20;           "City": data\["name"],

&#x20;           "Temperature\_C": data\["main"]\["temp"],

&#x20;           "Humidity\_%": data\["main"]\["humidity"],

&#x20;           "Weather\_Condition": data\["weather"]\[0]\["main"],

&#x20;           "Wind\_Speed\_mps": data\["wind"]\["speed"],

&#x20;           "Date\_Time": pd.to\_datetime(data\["dt"], unit="s")

&#x20;       })



df = pd.DataFrame(weather\_data)



print("\\nCleaned Weather Dataset:")

print(df)



df.to\_csv("weather\_data.csv", index=False)



print("\\nWeather data successfully saved to weather\_data.csv")



print("\\n--- BASIC WEATHER ANALYSIS ---")



highest\_temp = df.loc\[df\["Temperature\_C"].idxmax()]

highest\_humidity = df.loc\[df\["Humidity\_%"].idxmax()]

highest\_wind = df.loc\[df\["Wind\_Speed\_mps"].idxmax()]



print(f"Highest temperature: {highest\_temp\['City']} ({highest\_temp\['Temperature\_C']}°C)")

print(f"Highest humidity: {highest\_humidity\['City']} ({highest\_humidity\['Humidity\_%']}%)")

print(f"Highest wind speed: {highest\_wind\['City']} ({highest\_wind\['Wind\_Speed\_mps']} m/s)")



print("\\nWeather conditions by city:")

print(df\[\["City", "Weather\_Condition"]])

