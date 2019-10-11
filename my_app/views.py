from django.shortcuts import render
from django.http import JsonResponse
import json


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    name = postdata['name']
    username = postdata['username']
    email = postdata['email']
    phone = postdata['phone']
    password = postdata['password']
    
    if username is not None:
        issuccess= True
    else:
        issuccess= True

    datas = {
        'succes':True,
        'name':name
    }
    
    compt = 1
    while (compt < 100000):
        compt += 1
    
    return JsonResponse(datas, safe=False)