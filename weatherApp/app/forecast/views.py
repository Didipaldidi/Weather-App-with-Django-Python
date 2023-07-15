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
    result = {
        'region': soup.find("div", attrs={"id": "wob_loc"}).text,
        'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
        'dayhour': soup.find("div", attrs={"id": "wob_dts"}).text,
        'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
        'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text,
        'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
        'wind': soup.find("span", attrs={"id": "wob_ws"}).text,
        'next_days': []
    }
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        day_name = day.findAll("div")[0].attrs['aria-label']
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        max_temp = temp[0].text
        min_temp = temp[2].text
        result['next_days'].append({
            'name': day_name,
            'weather': weather,
            'max_temp': max_temp,
            'min_temp': min_temp
        })
    return result

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