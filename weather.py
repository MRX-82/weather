import requests
import logistic

lg = logistic.GpsWeather()
s_city = lg.s_city
city_id = lg.city_id
appid = lg.appid

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