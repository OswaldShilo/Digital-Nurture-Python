# Exercise 46: API Response Handler
# Objective: Parse JSON weather API response with error handling
# Note: Uses a simulated response — no network call needed to run

import json

class WeatherData:
    def __init__(self, city, temperature, condition):
        self.city        = city
        self.temperature = temperature
        self.condition   = condition

    def display(self):
        print(f"City        : {self.city}")
        print(f"Temperature : {self.temperature}°C")
        print(f"Condition   : {self.condition}")

def parse_weather(response_json):
    try:
        data = json.loads(response_json)
        if data.get("cod") == 404:
            print("Error 404: City not found.")
            return None
        return WeatherData(
            city        = data["name"],
            temperature = data["main"]["temp"],
            condition   = data["weather"][0]["description"]
        )
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
        return None

# Simulated API response
sample = json.dumps({
    "name": "Mumbai",
    "main": {"temp": 32.5},
    "weather": [{"description": "partly cloudy"}],
    "cod": 200
})

weather = parse_weather(sample)
if weather:
    weather.display()
