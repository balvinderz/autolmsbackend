import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from autolms.dolms import automate
# Create your views here.


def home(request):

    usernamefromuser = request.GET.get('emailid')

    passwordfromuser = request.GET.get('password')
    doquiz = request.GET.get("doquiz")
    dodiscussionform = request.GET.get("dodiscussionforum")
    print(type(doquiz))
    return automate(usernamefromuser, passwordfromuser, doquiz, dodiscussionform)
