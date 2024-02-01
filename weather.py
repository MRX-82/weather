import requests
import logistic

lg = logistic.GpsWeather()
s_city = lg.s_city
city_id = lg.city_id
appid = lg.appid


def wea_serch():
    """
    Weather on serch city
    """

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params = {'q': s_city, 'type': 'like', 'units': 'metric',
                                     'APPID': appid})
        data = res.json()
        cityes = ['{} ({})'.format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print('city:', cityes)
        city_id = data['list'][0]['id']
        print('city_id:', city_id)

    except Exception as e:
        print('Exception (find):', e)
        pass


def wea_five_day():
    """
    Weather on 5 day
    """
    
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru',
                               'APPID': appid})
        data=res.json()
        for i in data['list']:
            fd = (i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
            return fd
    except Exception as e:
        print("Exception (forecast)", e)
        pass


def wea_day():
    """
    Weather today
    """
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        conditions = ("conditions:", data['weather'][0]['description'])
        temp = ("temp:", data['main']['temp'])
        #temp_min = ("temp_min:", data['main']['temp_min'])
        #temp_max = ("temp_max:", data['main']['temp_max'])
        other_weather = [conditions, temp]
        return (other_weather)
    except Exception as e:
        print("Exception (weather):", e)
        pass

#weather = wea_five_day()