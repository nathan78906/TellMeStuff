from weather import Weather as WeatherApi, Unit
import requests

def get_weather(city):
    weather = WeatherApi(unit=Unit.CELSIUS)

    # Lookup via location name.

    location = weather.lookup_by_location(city)
    condition = location.condition()

    # Get weather forecasts for the upcoming days.

    result = location.location().city() + "," + location.location().country()
    result += "\nCurrent Temp: " + condition.temp() + " C"

    forecast = location.forecast()[0]
    result += "\nCondition: " + (forecast.text())
    result += "\nWith a high of " + forecast.high() + " C" + " and a low of " + forecast.low() + " C"
    return result

def get_quote():
    quotex = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
    word_content = quotex.json()
    quote = word_content["quoteText"]
    author = word_content["quoteAuthor"]
    body = quote + "\n -" + author
    return body
