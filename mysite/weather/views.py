from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import urllib.request
import json

def index(request):
    try:
        if request.method == "POST":
           latitude = request.POST['latitude']
           longitude = request.POST['longitude']
           choice = request.POST['choice']
           if choice == 'Current weather Minute forecast for 1 hour':
            response=requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+ latitude + '&lon=' + longitude + '&appid=dc3c506bb053361d700130f009aef134&units=metric').json()
            data = {
              'info' : response,
              'weather_data': response['weather'][0]
            }
            
           elif choice == 'Hourly forecast for 48 hours':
            response=requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=' + latitude + '&lon=' + longitude + '&appid=dc3c506bb053361d700130f009aef134&units=metric').json()
            data = {
                'info' : response
            }
            
           else:
            response=requests.get('api.openweathermap.org/data/2.5/forecast/daily?lat=' + latitude + '&lon=' + longitude + '&cnt={7}&appid=dc3c506bb053361d700130f009aef134&units=metric').json()
            data = {
                'info':response
            }
        
        else:
           data = {}
        return render(request,'index.html',data)

    except:
        return render(request, '404.html')
    
    