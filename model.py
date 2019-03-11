import requests
def by_city():
        city = input('Enter your city name : ')
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3cb7f658a281b611379c39ed305f441c&units=metric'.format(city)
        res = requests.get(url)
        data = res.json()
        return data
