from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests

def get_weather_forecast(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    forecast_data = response.json()
    return forecast_data

def details(request, city_name):
    api_key = ""  # Replace with your valid API key
    forecast_data = get_weather_forecast(city_name, api_key)

    # Extract the required data for the next 5 days
    if "list" in forecast_data:
        forecasts = forecast_data["list"][:40]  # 8 forecasts per day for 5 days
    else:
        forecasts = []

    # Prepare the data for rendering in the template
    weather_data = []
    for forecast in forecasts:
        weather_data.append({
            "datetime": forecast["dt_txt"],
            "temperature": forecast["main"]["temp"],
            "weather": forecast["weather"][0]["main"],
            "description": forecast["weather"][0]["description"]
        })

    context = {
        "city": city_name,
        "weather_data": weather_data,
    }

    return render(request, 'details.html', context)