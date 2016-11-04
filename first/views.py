from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse,Http404
import datetime

def index(request):
    list = "<html><body>now</body></html>"
    return HttpResponse(list)

def now(request):
    now = datetime.datetime.now()
    html = "<html><body>now: %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise  Http404()

    if(offset>=2):
        s = "s"
    else:
        s = ""
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour%s,it will be %s.</body><html>" %(offset,s,dt)
    return HttpResponse(html)
