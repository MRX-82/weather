import requests

s_city = "Razdol'noye, UA"
city_id = 0
appid = "cb85156c8938a7e9834aa53346a3f488"

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