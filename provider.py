import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s"


def k2c(temp):
    return int(temp - 273)

def get_weather(city, api_key):
    url = BASE_URL % (city, api_key)
    
    try:
        resp = requests.get(url)
        content = resp.json()
        city = content["city"]["name"]
        coord = content["city"]["coord"]
        country = content["city"]["country"]
        temps = content["list"]
        temp = temps[0]["main"]["temp"]
        weather = dict(city=city, coord=coord, country=country, temp = k2c(temp))
        return True, weather, None
    except Exception as e:
        print(e)
        return False, (), e