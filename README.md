This is a project in which I want to create a basic virtual assistan with whom you can talk about weather.

## Setup
Create the environment from the environment.yml file:
```bash
conda env create -f environment.yml
```
Remember to activate enviroment before use `conda activate weather-bot`.

## Running
weather-bot/bot.py --apikey XYZ

To get the OpenWeather API key visit: https://openweathermap.org/price and subscribe to get free access.

## Testing
To run tests type
```
python -m pytest tests/test_weather_bot.py
```

## Linting
To lint type
```
mypy bot
```
