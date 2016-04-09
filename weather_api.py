import requests

class WeatherApi(object):
    def __init__(self,retrieve):
        if retrieve == 'Fetch':
            self.response = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=dd6f2e0293494eb6a58230723162303&q=22408&num_of_days=1&format=xml&mca=no')
        else:
            self.response = None