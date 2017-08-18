from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
from first.models import Book

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

