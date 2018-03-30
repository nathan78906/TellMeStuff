from weather import Weather as WeatherApi, Unit
import requests
import praw
import json
import random
from django.conf import settings

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
    quotex = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en").content.decode('utf-8').replace("\\", "")
    word_content = json.loads(quotex)
    quote = word_content["quoteText"]
    author = word_content["quoteAuthor"]
    body = quote + "\n -" + author
    return body

def get_subreddit(sr):
    reddit = praw.Reddit(client_id=settings.REDDIT_CLIENT_ID, client_secret= settings.REDDIT_CLIENT_SECRET,
                         user_agent= settings.REDDIT_AUTH_AGENT)

    subreddit = reddit.subreddit(sr).top('day', limit=3)
    body = ''
    for x in subreddit:
        y = (x.title)
        z = (x.url)
        body += (y + '\n' + z + '\n\n')

    body = body.rstrip()
    return body

def get_urbandictionary():
    request = requests.get("http://urban-word-of-the-day.herokuapp.com/")
    word_content = request.json()
    word = word_content["word"]
    meaning = word_content["meaning"].replace("\n","")
    body = word + ":" + meaning
    body = body.rstrip()
    return body

def get_news():
    headers = {"Authorization" : "3198e3d3bdaa4520a987f190caa06a61"}
    request = requests.get(url="https://newsapi.org/v2/top-headlines?sources=google-news", headers=headers)
    news_content = request.json()
    news = news_content["articles"][0]
    title = news["title"]
    description = news["description"]
    news_url = news["url"]
    body = "Headline: " + title + "\n\n" + "Summary: " + description + "\n\n" + news_url
    return body

def get_photo():
    num = random.randint(0,997)
    photo_list = requests.get("https://picsum.photos/list").json()
    rand_photo = photo_list[num]
    author = rand_photo["author"]
    photo_id = rand_photo["id"]
    return {"author": author, "url": "https://picsum.photos/1920/1080?image=" + str(photo_id)}
