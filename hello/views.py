from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from .models import Greeting
from first.models import Book
from hello.models import Blog,Record
from .forms import RecordForm
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def book(request):
    books = Book.objects.all()
    return render(request,'book.html',{'books':books})

def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html',locals())

def record(request):
    if(request.method == 'GET'):
        form = RecordForm(request.GET)
        if(form.is_valid()):
            way = form.cleaned_data['way']
            strength = form.cleaned_data['strength']
            record = Record.objects.create(way = way,strength=strength)
            record.save()
            return HttpResponseRedirect('/record/')
    record = Record.objects.filter(date=datetime.now().date())
    form = RecordForm()
    print(datetime.now().date())
    return render(request,'record.html',locals())