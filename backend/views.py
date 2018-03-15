from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST

@csrf_protect
@require_POST
def dialogflow(request):
    json_data = request.body
    print(json_data)

    response = JsonResponse({"messages": [{"imageUrl": "https://i.imgur.com/kmyWgqH.jpg","platform": "facebook", "type": 3}]})

    #response = JsonResponse({"facebook": {"attachment":{"type":"image", "payload":{"url":"https://i.imgur.com/kmyWgqH.jpg", "is_reusable":"true"}}}})
    return response



