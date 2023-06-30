from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests, json
from .models import City
from .forms import CityForm, DeleteCityForm

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

def extract_weather_data(soup):
    weather_data = {}
    region_element = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    weather_data['region'] = region_element.text if region_element else ''

    temp_now_element = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    weather_data['temp_now'] = temp_now_element.text if temp_now_element else ''

    dayhour_element = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    if dayhour_element:
        weather_data['dayhour'], weather_data['weather_now'] = dayhour_element.text.split('\n')
    else:
        weather_data['dayhour'] = ''
        weather_data['weather_now'] = ''

    return weather_data

def get_current_loc_info():
    try:
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = ip.json()
        res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
        location_data = res.json()
        html_content = get_html_content(location_data)
        soup = BeautifulSoup(html_content, 'html.parser')
        weather_data = extract_weather_data(soup)
        return location_data, weather_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during API request: {str(e)}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"An error occurred while parsing JSON: {str(e)}")

def get_weather_db(city):
    location_data = {'city': city}
    html_content = get_html_content(location_data)
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_data = extract_weather_data(soup)
    return weather_data

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm()
    return render(request, 'weather/add_city.html', {'form': form})

def delete_city(request):
    if request.method == 'POST':
        form = DeleteCityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            City.objects.filter(name=city_name).delete()
            return redirect('city_list')
    else:
        form = DeleteCityForm()
    return render(request, 'weather/delete_city.html', {'form': form})

def index(request):
    current_loc = get_current_loc_info()
    cities = City.objects.all()
    weathers_data = []

    for city in cities:
        city_weather = get_weather_db(city.name)
        weathers_data.append(city_weather)

    context = {
        'location_data': current_loc[0],
        'weather_data': current_loc[1],
        'ls_of_weather': weathers_data,
    }

    return render(request, 'weather/index.html', context) #returns the index.html template 