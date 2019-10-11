import uuid
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from autolms.dolms import automate
# Create your views here.


def home(request):

    #driver = webdriver.Chrome(r'/Users/balvinder/Documents/ring/chromedriver')
    usernamefromuser = request.GET.get('emailid')

    passwordfromuser = request.GET.get('password')
    automate(usernamefromuser, passwordfromuser)
    return HttpResponse(uuid.uuid1())
