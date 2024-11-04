from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "template.html")

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def proxy_square(request):
    if request.method == 'POST':
        side_data = json.loads(request.body)
        response = requests.post("http://34.101.132.69:8080/function/service-square", json=side_data)
        return JsonResponse(response.json())

@csrf_exempt
def proxy_cube(request):
    if request.method == 'POST':
        side_data = json.loads(request.body)
        response = requests.post("http://34.101.96.16:8080/function/service-cube", json=side_data)
        return JsonResponse(response.json())
