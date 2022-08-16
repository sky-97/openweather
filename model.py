import requests
def by_city():
        city = input('Enter your city name : ')
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=apikey&units=metric'.format(city)
        res = requests.get(url)
        data = res.json()
        return data
