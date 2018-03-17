from django.shortcuts import render, redirect
import json
from weather import Weather, Unit

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def dialogflow(request):
    json_data = request.body
    print(json_data)

    weather = Weather(unit=Unit.CELSIUS)

    # Lookup via location name.

    location = weather.lookup_by_location('toronto')
    condition = location.condition()

    # Get weather forecasts for the upcoming days.

    string = location.location().city() + "," + location.location().country()
    string += "\nCurrent Temp: " + condition.temp() + " C"

    forecast = location.forecast()[0]
    string += "\nCondition: " + (forecast.text())
    string += "\nWith a high of " + forecast.high() + " C"
    string += "\nand a low of " + forecast.low() + " C"

    response = JsonResponse({"messages": [{"platform": "facebook","speech": string,"type": 0}]})
    #response = JsonResponse({"messages": [{"imageUrl": "https://i.imgur.com/kmyWgqH.jpg","platform": "facebook", "type": 3}]})

    #response = JsonResponse({"facebook": {"attachment":{"type":"image", "payload":{"url":"https://i.imgur.com/kmyWgqH.jpg", "is_reusable":"true"}}}})
    return response

def home(request):
    response = JsonResponse({"hi": "ayy"})
    return response

def index(request):
    return render(request, 'backend/index.html')
