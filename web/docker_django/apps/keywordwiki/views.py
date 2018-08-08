from django.shortcuts import render, redirect
from redis import Redis


#redis = Redis(host='redis', port=6379)


def home(request):
    #counter = redis.incr('counter')
    counter = 0
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
