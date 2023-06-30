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

def get_current_loc_info():
    ip = requests.get('https://api.ipify.org?format=json')# url for the ip api
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])# url for the geolocation api and pass the api address of the user
    temp = res.text
    location_data = json.loads(temp)# convert json to python dict

    weather_data = None #use to store the weather information

    # fetch the weather from Google.
    html_content = get_html_content(location_data)
    soup = BeautifulSoup(html_content, 'html.parser')
    weather_data = dict()
    # extract region
    weather_data['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    # extract temperature now
    weather_data['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    # get the day, hour and actual weather
    weather_data['dayhour'], weather_data['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
    return (location_data, weather_data)

def get_weather_db(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+{city}').text #get the weather information from webscraping

    weather_data = None

    soup = BeautifulSoup(html_content, 'html.parser')
    weather_data = dict()

    region_element = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    if region_element:
        weather_data['region'] = region_element.text
    else:
        weather_data['region'] = ''

    temp_now_element = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    if temp_now_element:
        weather_data['temp_now'] = temp_now_element.text
    else:
        weather_data['temp_now'] = ''

    dayhour_element = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"})
    if dayhour_element:
        weather_data['dayhour'], weather_data['weather_now'] = dayhour_element.text.split('\n')
    else:
        weather_data['dayhour'] = ''
        weather_data['weather_now'] = ''

    return weather_data

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')  # Redirect to a success page or a different view
    else:
        form = CityForm()
    
    return render(request, 'weather/add_city.html', {'form': form})

def delete_city(request):
    if request.method == 'POST':
        form = DeleteCityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            City.objects.filter(name=city_name).delete()
            return redirect('city_list')  # Redirect to the index view after deleting the city
    else:
        form = DeleteCityForm()

    return render(request, 'weather/delete_city.html', {'form': form})

def index(request):
    current_loc = get_current_loc_info() # contains the weather inforamtion of current location
    cities = City.objects.all()# return all the cities in the database
    weathers_data = []

    for city in cities:
        city_weather = get_weather_db(city.name)
        weathers_data.append(city_weather)
    
    return render(request, 'weather/index.html', {'location_data': current_loc[0], 'weather_data': current_loc[1], 'ls_of_weather': weathers_data,},) #returns the index.html template 