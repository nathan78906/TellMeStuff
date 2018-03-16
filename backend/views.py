from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

@csrf_exempt
def dialogflow(request):
    json_data = request.body
    response = JsonResponse({"messages": [{"imageUrl": "https://i.imgur.com/kmyWgqH.jpg","platform": "facebook", "type": 3}]})

    #response = JsonResponse({"facebook": {"attachment":{"type":"image", "payload":{"url":"https://i.imgur.com/kmyWgqH.jpg", "is_reusable":"true"}}}})
    return response



