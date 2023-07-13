from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import urllib.request
import json



# Create your views here.
def index(request):
    try:
        if request.method == "POST":
           latitude = request.POST['latitude']
           longitude = request.POST['longitude']
           response=requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+ latitude + '&lon=' + longitude + '&appid=dc3c506bb053361d700130f009aef134&units=metric').json()
           data = {
              'info' : response,
              'weather_data': response['weather'][0]
            }
        else:
           data = {}
        return render(request,'index.html',data)

    except:
        return render(request, '404.html')
    # response=requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=dc3c506bb053361d700130f009aef134')
    # users = response.json()
    # print(users)
    # return render(request,'index.html')
    