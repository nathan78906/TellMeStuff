from django.shortcuts import render, redirect
import json
from weather import Weather as WeatherApi, Unit
import requests
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

from .models import Weather, Profile, Subreddit, Motivation, UrbanDictionary, News, Photo

from .services import get_weather, get_quote, get_subreddit, get_urbandictionary, get_news, get_photo

# Manages communication between FB/SMS and backend
# Adds facebook user ID mapping
# Calls APIs for subscriptions
# Intent matching for specific subscriptions
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
            entry = Profile.objects.get(user=user)
            entry.facebook_id = body["originalRequest"]["data"]["sender"]["id"]
            entry.save()
            return HttpResponse(status=200)
        else:
            try:
                profile_entry = Profile(user=user, facebook_id=body["originalRequest"]["data"]["sender"]["id"])
                profile_entry.save()
                return HttpResponse(status=200)            
            except:
                return HttpResponse("Internal server error", status=500)
    
    if body["originalRequest"]["source"] == "twilio":
        if Profile.objects.filter(phone_number=body["originalRequest"]["data"]["From"][2:]).exists():
            user = Profile.objects.get(phone_number=body["originalRequest"]["data"]["From"][2:]).user
            username = user.username
            welcome = "Here's stuff for " + username
            json_ret = {"messages": [{"speech": welcome,"type": 0}]}
            
            if body["result"]["metadata"]["intentName"] == "weather":
                if Weather.objects.filter(user=user).exists():
                    if Weather.objects.get(user=user).active:
                        city = Weather.objects.get(user=user).location
                        result = get_weather(city)
                        json_ret["messages"].append({"speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "subreddit":
                if Subreddit.objects.filter(user=user).exists():
                    if Subreddit.objects.get(user=user).active:
                        sr = Subreddit.objects.get(user=user).subreddit
                        result = get_subreddit(sr)
                        json_ret["messages"].append({"speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "motivation":
                if Motivation.objects.filter(user=user).exists():
                    if Motivation.objects.get(user=user).active:
                        result = get_quote()
                        json_ret["messages"].append({"speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "wordoftheday":
                if UrbanDictionary.objects.filter(user=user).exists():
                    if UrbanDictionary.objects.get(user=user).active:
                        result = get_urbandictionary()
                        json_ret["messages"].append({"speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "news":
                if News.objects.filter(user=user).exists():
                    if News.objects.get(user=user).active:
                        result = get_news()
                        json_ret["messages"].append({"speech": result,"type": 0})
            # photo not available on SMS
            elif body["result"]["metadata"]["intentName"] == "photo":
                return JsonResponse({"speech": "Random Photo is not available on SMS","type": 0})
            else:
                if Weather.objects.filter(user=user).exists():
                    if Weather.objects.get(user=user).active:
                        city = Weather.objects.get(user=user).location
                        result = get_weather(city)
                        json_ret["messages"].append({"speech": result,"type": 0})

                if Motivation.objects.filter(user=user).exists():
                    if Motivation.objects.get(user=user).active:
                        result = get_quote()
                        json_ret["messages"].append({"speech": result,"type": 0})

                if UrbanDictionary.objects.filter(user=user).exists():
                    if UrbanDictionary.objects.get(user=user).active:
                        result = get_urbandictionary()
                        json_ret["messages"].append({"speech": result,"type": 0})

                if Subreddit.objects.filter(user=user).exists():
                    if Subreddit.objects.get(user=user).active:
                        sr = Subreddit.objects.get(user=user).subreddit
                        result = get_subreddit(sr)
                        json_ret["messages"].append({"speech": result,"type": 0})

                if News.objects.filter(user=user).exists():
                    if News.objects.get(user=user).active:
                        result = get_news()
                        json_ret["messages"].append({"speech": result,"type": 0})
            
            print(json_ret)
            if len(json_ret["messages"]) == 1:
                response = JsonResponse({"messages": [{"speech": "No active subscriptions for " + username,"type": 0}]})
            else:
                response = JsonResponse(json_ret)
        else:
            response = JsonResponse({"messages": [{"speech": "No match found!","type": 0}]})
    elif body["originalRequest"]["source"] == "facebook":
        if Profile.objects.filter(facebook_id=body["originalRequest"]["data"]["sender"]["id"]).exists():
            user = Profile.objects.get(facebook_id=body["originalRequest"]["data"]["sender"]["id"]).user
            username = user.username
            welcome = "Here's stuff for " + username
            json_ret = {"messages": [{"platform": "facebook","speech": welcome,"type": 0}]}
            
            if body["result"]["metadata"]["intentName"] == "weather":
                if Weather.objects.filter(user=user).exists():
                    if Weather.objects.get(user=user).active:
                        city = Weather.objects.get(user=user).location
                        result = get_weather(city)
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "subreddit":
                if Subreddit.objects.filter(user=user).exists():
                    if Subreddit.objects.get(user=user).active:
                        sr = Subreddit.objects.get(user=user).subreddit
                        result = get_subreddit(sr)
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "motivation":
                if Motivation.objects.filter(user=user).exists():
                    if Motivation.objects.get(user=user).active:
                        result = get_quote()
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "wordoftheday":
                if UrbanDictionary.objects.filter(user=user).exists():
                    if UrbanDictionary.objects.get(user=user).active:
                        result = get_urbandictionary()
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "news":
                if News.objects.filter(user=user).exists():
                    if News.objects.get(user=user).active:
                        result = get_news()
                        json_ret["messages"].append({"platform": "facebook", "speech": result,"type": 0})
            elif body["result"]["metadata"]["intentName"] == "photo":
                if Photo.objects.filter(user=user).exists():
                    if Photo.objects.get(user=user).active:
                        photo = get_photo()
                        json_ret["messages"].append({"buttons": [{"postback": photo["source"] ,"text": "Photo Source"}],"imageUrl": photo["url"],"platform": "facebook","title": photo["author"],"type": 1})
            else:
                if Weather.objects.filter(user=user).exists():
                    if Weather.objects.get(user=user).active:
                        city = Weather.objects.get(user=user).location
                        result = get_weather(city)
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})

                if Motivation.objects.filter(user=user).exists():
                    if Motivation.objects.get(user=user).active:
                        result = get_quote()
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})

                if UrbanDictionary.objects.filter(user=user).exists():
                    if UrbanDictionary.objects.get(user=user).active:
                        result = get_urbandictionary()
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})

                if Subreddit.objects.filter(user=user).exists():
                    if Subreddit.objects.get(user=user).active:
                        sr = Subreddit.objects.get(user=user).subreddit
                        result = get_subreddit(sr)
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})
                
                if News.objects.filter(user=user).exists():
                    if News.objects.get(user=user).active:
                        result = get_news()
                        json_ret["messages"].append({"platform": "facebook","speech": result,"type": 0})

                if Photo.objects.filter(user=user).exists():
                    if Photo.objects.get(user=user).active:
                        photo = get_photo()
                        json_ret["messages"].append({"buttons": [{"postback": photo["source"] ,"text": "Photo Source"}],"imageUrl": photo["url"],"platform": "facebook","title": photo["author"],"type": 1})
            
            print(json_ret)
            if len(json_ret["messages"]) == 1:
                response = JsonResponse({"messages": [{"platform": "facebook","speech": "No active subscriptions for " + username,"type": 0}]})
            else:
                response = JsonResponse(json_ret)
        else:
            response = JsonResponse({"messages": [{"platform": "facebook","speech": "No match found!","type": 0}]})
    return response

# signs up a user
def api_signup(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            username = body['username']
            password = body['password']
            password_confirm = body['password_confirm']
        except:
            return HttpResponse("One or more parameters are missing", status=400)
        if len(password) < 6:
            return HttpResponse("Password must be at least 6 characters long!", status=422) 
        if password != password_confirm:
            return HttpResponse("Passwords do not match", status=422) 

        try:
          user = User.objects.create_user(username=username, password=password)
          user.save()
        except:
          return HttpResponse("Username already exists", status=409)
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return JsonResponse({"username": username})
    else:
        return HttpResponse("Method not allowed", status=405)

# signs in a user
def api_signin(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            username = body['username']
            password = body['password']
        except:
            return HttpResponse("One or more parameters are missing", status=400)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"username": username})
        else:
            return HttpResponse("Invalid credentials", status=401)
    return HttpResponse("Method not allowed", status=405)

# logs out a user and redirects to homepage
def api_logout(request):
    if request.method == "GET":
        try:
            logout(request)
            return redirect("/")
        except:
            return HttpResponse("Invalid credentials", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)

# Stores the user's location in the database for use in the weather subscription
def set_location(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                location = body['location']
            except:
                return HttpResponse("One or more parameters are missing", status=400)
            try:
                get_weather(location)
            except:
                return HttpResponse("Invalid location", status=400)
            if Weather.objects.filter(user = request.user).exists():
                entry = Weather.objects.get(user = request.user)
                entry.location = location
                entry.save()
                return JsonResponse({"location": location})
            else:
                try:
                    weather_entry = Weather(user=request.user, location=location)
                    weather_entry.save()
                    return JsonResponse({"location": location})            
                except:
                    return HttpResponse("Internal server error", status=500)
        else:
            return HttpResponse("Access Denied", status=401)                
    else:
        return HttpResponse("Method not allowed", status=405)

# Gives the user a subreddit example and checks their subscription status
def subreddit(request):
    if request.method == "POST" or request.method == "GET":
        if request.user.is_authenticated:
            if request.method == "POST":
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                try:
                    subreddit = body['subreddit']
                except:
                    return HttpResponse("One or more parameters are missing", status=400)
                try:
                    get_subreddit(subreddit)
                except:
                    return HttpResponse("Invalid subreddit", status=400)
                if Subreddit.objects.filter(user = request.user).exists():
                    entry = Subreddit.objects.get(user = request.user)
                    entry.subreddit = subreddit
                    entry.save()
                    return JsonResponse({"subreddit": subreddit})
                else:
                    try:
                        subreddit_entry = Subreddit(user=request.user, subreddit=subreddit)
                        subreddit_entry.save()
                        return JsonResponse({"subreddit": subreddit})            
                    except:
                        return HttpResponse("Internal server error", status=500)
            elif request.method == "GET":
                if Subreddit.objects.filter(user = request.user).exists():
                    entry = Subreddit.objects.get(user = request.user)
                    return JsonResponse({"subreddit": entry.subreddit, "active": entry.active})
                else:
                    return JsonResponse({"subreddit": "", "active": ""})
        else:
            return HttpResponse("Access Denied", status=401)         
    else:
        return HttpResponse("Method not allowed", status=405)       

# Stores a user's phone number in the database
def phonenumber(request):
    if request.method == "POST" or request.method == "GET":
        if request.user.is_authenticated:
            if request.method == "POST":
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                try:
                    phone_number = body['phone_number']
                except:
                    return HttpResponse("One or more parameters are missing", status=400)
                if len(phone_number) < 10 or not(phone_number.isdigit()):
                    return HttpResponse("Phone number must be at least 10 digits long!", status=422)
                try:
                    profile_entry = Profile.objects.get(user=request.user)
                    profile_entry.phone_number = phone_number
                    profile_entry.save()
                    return JsonResponse({"phone_number": phone_number})
                except:
                    profile_entry = Profile(user=request.user, phone_number=phone_number)
                    profile_entry.save()
                    return JsonResponse({"phone_number": phone_number}) 
            elif request.method == "GET":
                if Profile.objects.filter(user=request.user).exists():
                    entry = Profile.objects.get(user=request.user)
                    return JsonResponse({"phone_number": entry.phone_number})
                else:
                    return JsonResponse({"phone_number": ""})
        else:
            return HttpResponse("Access Denied", status=401)     
    else:
        return HttpResponse("Method not allowed", status=405)           
       
# Sets the subscriptions to off or on based on subscription type
def toggle(request):
    if request.method == "PATCH":
        if request.user.is_authenticated:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                action = body['action']
                toggle_type = body['type']    
            except:
                return HttpResponse("One or more parameters are missing", status=400)
            if toggle_type == "weather":
                if Weather.objects.filter(user = request.user).exists():
                    entry = Weather.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    return HttpResponse("Please submit a location first", status=500)
            elif toggle_type == "motivation":
                if Motivation.objects.filter(user = request.user).exists():
                    entry = Motivation.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    try:
                        entry = Motivation(user = request.user, active = action)
                        entry.save()
                        return JsonResponse({"type": toggle_type, "action": action})             
                    except:
                        return HttpResponse("Internal server error", status=500)
            elif toggle_type == "subreddit":
                if Subreddit.objects.filter(user = request.user).exists():
                    entry = Subreddit.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    return HttpResponse("Please submit a subreddit first", status=500)
            elif toggle_type == "urban":
                if UrbanDictionary.objects.filter(user = request.user).exists():
                    entry = UrbanDictionary.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    try:
                        entry = UrbanDictionary(user = request.user, active = action)
                        entry.save()
                        return JsonResponse({"type": toggle_type, "action": action})             
                    except:
                        return HttpResponse("Internal server error", status=500)
            elif toggle_type == "news":
                if News.objects.filter(user = request.user).exists():
                    entry = News.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    try:
                        entry = News(user = request.user, active = action)
                        entry.save()
                        return JsonResponse({"type": toggle_type, "action": action})             
                    except:
                        return HttpResponse("Internal server error", status=500)
            elif toggle_type == "photo":
                if Photo.objects.filter(user = request.user).exists():
                    entry = Photo.objects.get(user = request.user)
                    entry.active = action
                    entry.save()
                    return JsonResponse({"type": toggle_type, "action": action})
                else:
                    try:
                        entry = Photo(user = request.user, active = action)
                        entry.save()
                        return JsonResponse({"type": toggle_type, "action": action})             
                    except:
                        return HttpResponse("Internal server error", status=500)
        else:
            return HttpResponse("Access Denied", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)                        

# Gets the user's ID for the facebook messenger link
def user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if Profile.objects.filter(user=request.user).exists():
                return JsonResponse({"user_id": request.user.id, "user_name": request.user.username, "profile": True})
            else:
                return JsonResponse({"user_id": request.user.id, "user_name": request.user.username, "profile": False})   
        else:
            return HttpResponse("Access Denied", status=401)             
    else:
        return HttpResponse("Method not allowed", status=405)

# Checks the state of a user's weather subscription
def getWeather(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if Weather.objects.filter(user = request.user).exists():
                entry = Weather.objects.get(user = request.user)
                return JsonResponse({"location": entry.location, "active": entry.active})
            else:
                return JsonResponse({"location": "", "active": ""})
        else:
            return HttpResponse("Access Denied", status=401)         
    else:
        return HttpResponse("Method not allowed", status=405)   

# Gives the user a quote example
def getQuote(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            body = get_quote()
            return JsonResponse({"content": body})
        else:
            return HttpResponse("Access Denied", status=401)        
    else:
        return HttpResponse("Method not allowed", status=405)

# Checks the state of a user's motivational quote subscription
def getMotivation(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if Motivation.objects.filter(user = request.user).exists():
                entry = Motivation.objects.get(user = request.user)
                return JsonResponse({"active": entry.active})
            else:
                return JsonResponse({"active": ""})
        else:
            return HttpResponse("Access Denied", status=401)      
    else:
        return HttpResponse("Method not allowed", status=405)      

# Gives the user a word of the day example
def getUWordOfTheDay(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            body = get_urbandictionary()
            return JsonResponse({"content": body})
        else:
            return HttpResponse("Access Denied", status=401)        
    else:
        return HttpResponse("Method not allowed", status=405)             

# Checks the state of a user's word of the day subscription
def getUrbanDictionary(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if UrbanDictionary.objects.filter(user = request.user).exists():
                entry = UrbanDictionary.objects.get(user = request.user)
                return JsonResponse({"active": entry.active})
            else:
                return JsonResponse({"active": ""})
        else:
            return HttpResponse("Access Denied", status=401)  
    else:
        return HttpResponse("Method not allowed", status=405)                       

# Gives the user a news example
def news_example(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            body = get_news()
            return JsonResponse({"content": body})
        else:
            return HttpResponse("Access Denied", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)                     

# Gives the user a reddit example
def reddit_example(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            body = get_subreddit("all")
            return JsonResponse({"content": body})
        else:
            return HttpResponse("Access Denied", status=401) 
    else:
        return HttpResponse("Method not allowed", status=405)                    

# Checks the state of a user's news subscription
def news(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if News.objects.filter(user = request.user).exists():
                entry = News.objects.get(user = request.user)
                return JsonResponse({"active": entry.active})
            else:
                return JsonResponse({"active": ""})
        else:
            return HttpResponse("Access Denied", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)                         

# Checks the state of a user's photo subscription
def photo(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if Photo.objects.filter(user = request.user).exists():
                entry = Photo.objects.get(user = request.user)
                return JsonResponse({"active": entry.active})
            else:
                return JsonResponse({"active": ""})
        else:
            return HttpResponse("Access Denied", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)             

# Gives the user a photo example
def photo_example(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            body = get_photo()
            return JsonResponse(body)
        else:
            return HttpResponse("Access Denied", status=401)
    else:
        return HttpResponse("Method not allowed", status=405)             

# Redirects user to main page
def index(request):
    return render(request, 'backend/index.html')

# Checks if user is authenticated and redirects the user to credits page
def credits(request):
    if request.user.is_authenticated:
        return render(request, 'backend/credits_loggedin.html')
    return render(request, 'backend/credits.html')

# Checks if user is authenticated and redirects the user to documentation page 
def documentation(request):
    if request.user.is_authenticated:
        return render(request, 'backend/api_documentation_loggedin.html')
    return render(request, 'backend/api_documentation.html')

# Checks if user is authenticated and redirects the user to signup page or dashboard
def signup(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return render(request, 'backend/signup.html')

# Checks if user is authenticated and redirects the user to signin page or dashboard
def signin(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return render(request, 'backend/signin.html')    

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard.html') 

@login_required
def profile(request):
    return render(request, 'backend/profile.html')
