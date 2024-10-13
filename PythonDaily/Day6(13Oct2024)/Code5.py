# Write a Python program using the requests module to send a GET request to a public API (e.g., fetching weather data), and then parse and display the data.

import requests
import json

# Set API endpoint and API key
API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY_HERE"

# Set city and country code
CITY = "London"
COUNTRY_CODE = "UK"

# Construct API request URL
url = f"{API_ENDPOINT}?q={CITY},{COUNTRY_CODE}&appid={API_KEY}"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract relevant weather data
    weather_data = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"] - 273.15,  # Convert Kelvin to Celsius
        "Humidity (%)": data["main"]["humidity"],
        "Weather Description": data["weather"][0]["description"]
    }

    # Display weather data
    print("Weather Data:")
    for key, value in weather_data.items():
        print(f"{key}: {value}")
else:
    print("Error:", response.status_code)