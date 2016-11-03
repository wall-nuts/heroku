from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>now: %s .</body></html>" % now
    return HttpResponse(html)
