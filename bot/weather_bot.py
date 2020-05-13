from jsgf import parse_grammar_string
import requests 
import json

class WeatherBot:
    """Bot for checking the weather"""
    def __init__(self, grammar_path, api_key):
        with open(grammar_path) as myf:
            data = myf.read()

        self.grammar = parse_grammar_string(data)
        self.api_key = api_key

    def __check_weather(self):
        city = 'warsaw'
        country = 'poland'
        weather_data = self.__get_weather_from_api(city, country, self.api_key)
        return "In {} the temperature is {}".format(weather_data['name'], weather_data['main']['temp'])

    def response(self, user_input):
        rule = self.grammar.find_matching_rules(user_input)
        if rule and rule[0].name == "CHECK_WEATHER":
            return self.__check_weather()
        else:
            return "I don't know what you're talking about"

    def __get_weather_from_api(self, city, country, api_key):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}'.format(city, country, api_key))
        return json.loads(r.text)
