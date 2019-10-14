import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from autolms.dolms import automate
# Create your views here.


def home(request):

    usernamefromuser = request.GET.get('emailid')

    passwordfromuser = request.GET.get('password')
    doquiz = int(request.GET.get("doquiz"))
    print(doquiz)
    dodiscussionform = int(request.GET.get("dodiscussionform"))
    print(dodiscussionform)
    return HttpResponse(automate(usernamefromuser, passwordfromuser, doquiz, dodiscussionform))
