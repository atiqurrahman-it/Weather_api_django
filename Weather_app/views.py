from django.shortcuts import render
from .models import weather_model

import requests


# Create your views here.
# {'coord': {'lon': 90.4074, 'lat': 23.7104},
#  'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}],
#  'base': 'stations',
#  'main':{'temp': 68, 'feels_like': 66.25, 'temp_min': 68, 'temp_max': 68, 'pressure': 1015, 'humidity': 68},
#  'visibility': 3500, 'wind': {'speed': 7.05, 'deg': 316}, 'clouds': {'all': 0}, 'dt': 1612808640,
#  'sys': {'type': 1, 'id': 9145, 'country': 'BD', 'sunrise': 1612830918, 'sunset': 1612871398},
#  'timezone': 21600, 'id': 1185241, 'name': 'Dhaka', 'cod': 200}

def Homepage(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8bbc87f00eca50610298990b22b5d8fd'
    if request.method == 'POST':
        city_name = request.POST.get('city_add')
        data = weather_model(City=city_name)
        data.save()


    last_data = weather_model.objects.latest('id')
    city = last_data
    value_store = requests.get(url.format(city)).json()

    weather_all_value = {
        'City': city,
        'contr': value_store['sys']['country'],
        'icon': value_store['weather'][0]['icon'],
        'temperature': value_store['main']['temp'],
        'details': value_store['weather'][0]['description'],
        "last_data": last_data,
    }
    data = {
        "weather": weather_all_value,
    }

    return render(request, 'index.html', data)
