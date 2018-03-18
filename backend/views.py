from django.shortcuts import render, redirect
import json
from weather import Weather, Unit

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

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

@csrf_exempt
def api_signup(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    password_confirm = body['password_confirm']
    if password != password_confirm:
        return HttpResponse("Passwords do not match", status=422) 
    try:
      user = User.objects.create_user(username=username, password=password)
      user.save()
    except:
      return HttpResponse("Username already exists", status=409)
    
    return HttpResponse(status=200)


@csrf_exempt
def api_signin(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(status=200) 
    else:
        return HttpResponse("Invalid credentials", status=401)

@csrf_exempt
def api_logout(request):
    logout(request)
    return redirect("/")

def home(request):
    response = JsonResponse({"hi": "ayy"})
    return response

def index(request):
    return render(request, 'backend/index.html')

def signup(request):
    return render(request, 'backend/signup.html')

def signin(request):
    return render(request, 'backend/signin.html')    

def dashboard(request):
    return render(request, 'backend/dashboard.html') 

def profile(request):
    return render(request, 'backend/profile.html')
