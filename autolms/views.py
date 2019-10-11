from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from django.http import JsonResponse
import json
# Create your views here.
def home(request):
    
    driver = webdriver.Chrome(r'/Users/balvinder/Documents/ring/chromedriver')
    driver.get("https://google.com")

    

    return HttpResponse(request.GET.get('emailid'))
