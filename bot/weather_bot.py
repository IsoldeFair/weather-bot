"""An agent that interprets the intentions of user input and prepares an accurate response.
It can check the weather in a particular city or country.

  Typical usage example:
  weather_check = WeatherBot("./grammars/weather.jsgf", args."SECRET_KEY")
  response = weather_check.response("Check weather in New York")
"""

import json
import requests
from typing import Dict
from jsgf import parse_grammar_string

class WeatherBot(object):
    """Bot for checking the weather"""
    def __init__(self, grammar_path: str, api_key: str) -> None:
        with open(grammar_path) as myf:
            data = myf.read()

        self.grammar = parse_grammar_string(data)
        self.api_key = api_key

    def __check_weather(self, city: str='warsaw', country: str='poland') -> str:
        """Forms a full response for the user about the weather conditions in a particular city.

        Args:
          city: name of the city
          country: name of the country the city is in

        Returns:
          Bot response to the user with the information about the weather in searched location.
        """
        weather_data = self.__get_weather_from_api(city, country, self.api_key)
        return "In {} the temperature is {}".format(weather_data['name'], \
                weather_data['main']['temp'])

    def response(self, user_input: str) -> str:
        """Checks the user intentions and prepares a response.

        Args:
          user_input: what the user asked the bot

        Returns:
          The accurate response for user intentions.
          If not recognized, the bot responds that it does not understand.
        """
        rule = self.grammar.find_matching_rules(user_input)
        if rule and rule[0].name == "CHECK_WEATHER":
            return self.__check_weather()
        return "I don't know what you're talking about"

    def __get_weather_from_api(self, city: str, country: str, api_key: str) -> Dict:
        """Sends a request to OpenWeather API.

        Args:
          city: name of the city
          country: name of the country the city is in
          api_key: API key to OpenWeather

        Returns:
          API response in json format.
        """
        openweather_url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&APPID={}'
        req = requests.get(openweather_url.format(city, country, api_key))
        return json.loads(req.text)
