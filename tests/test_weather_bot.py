import pytest
from bot.weather_bot import WeatherBot


class TestWeatherBot:
    
    @pytest.mark.parametrize(("user_input", "expected_response"),
            [
                ("check weather", "In warsaw the temperature is 286.0"),
                ("blablabla", "I don't know what you're talking about"),
            ]
    )
    def test_response(self, user_input, expected_response):
        weather_check = WeatherBot("./grammars/weather.jsgf", "SECRET_KEY")
        assert weather_check.response(user_input) == expected_response
