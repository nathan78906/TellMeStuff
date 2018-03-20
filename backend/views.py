from django.shortcuts import render, redirect
import json
from weather import Weather as WeatherApi, Unit

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from .models import Weather, Profile

@csrf_exempt
@require_POST
def dialogflow(request):
    json_data = request.body
    print(json_data)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    if body["result"]["resolvedQuery"] == "FACEBOOK_WELCOME":
        # get user that matches userID
        user_id = int(body["originalRequest"]["data"]["postback"]["referral"]["ref"])
        user = User.objects.get(pk=user_id)
        if Profile.objects.filter(user=user).exists():
            entry = Weather.objects.get(user = request.user)
            entry.facebook_id = body["originalRequest"]["data"]["sender"]["id"]
            entry.save()
            return HttpResponse(status=200)
        else:
            try:
                profile_entry = Profile(user=user, facebook_id = body["originalRequest"]["data"]["sender"]["id"])
                profile_entry.save()
                return HttpResponse(status=200)            
            except:
                return HttpResponse("Internal server error", status=500)


    weather = WeatherApi(unit=Unit.CELSIUS)

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

@csrf_exempt
def set_location(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    location = body['location']
    if Weather.objects.filter(user = request.user).exists():
        entry = Weather.objects.get(user = request.user)
        entry.location = location
        entry.save()
        return HttpResponse(status=200)
    else:
        try:
            weather_entry = Weather(user=request.user, location=location)
            weather_entry.save()
            return HttpResponse(status=200)            
        except:
            return HttpResponse("Internal server error", status=500)
        

def home(request):
    response = JsonResponse({"hi": "ayy"})
    return response

def index(request):
    return render(request, 'backend/index.html')

def signup(request):
    return render(request, 'backend/signup.html')

def signin(request):
    return render(request, 'backend/signin.html')    

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard.html') 

@login_required
def profile(request):
    return render(request, 'backend/profile.html')
