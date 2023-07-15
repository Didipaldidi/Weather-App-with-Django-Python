from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests

# Create your views here.
def get_html_content(location_data):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = location_data['city']
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content


def get_weather_data(html_content):
    soup = bs(html_content, "html.parser")
    forecast_elems = soup.select('.tAd8D')

    forecast_data = []
    for elem in forecast_elems:
        day = elem.select_one('.SUZt4c-d0F2t').text
        weather = elem.select_one('.eIuuYe-tzA9Ye span').get('aria-label')
        temp_high = elem.select_one('.wxData span:first-child').text
        temp_low = elem.select_one('.wxData span:last-child').text

        forecast_data.append({
            'day': day,
            'weather': weather,
            'temp_high': temp_high,
            'temp_low': temp_low
        })

    return forecast_data

def details(request):
    location_data = {
        'city': 'New York',  # Replace 'YourCity' with the actual city name
    }
    html_content = get_html_content(location_data)
    weather_data = get_weather_data(html_content)

    context = {
        'weather_data': weather_data,
    }

    return render(request, 'details.html', context)