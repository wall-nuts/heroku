#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from .models import Greeting
from first.models import Book
from hello.models import Blog,Record
from .forms import RecordForm
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

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
    books = Book.objects.all()[::-1]
    paginator = Paginator(books,30.2)
    page = request.GET.get('page')
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request,'book.html',{"books":books,"book":book})

def book_detail(request):
    d

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
    now = datetime.now()
    record = Record.objects.filter(date__year=now.year,date__month=now.month,date__day=now.day)
    form = RecordForm()
    return render(request,'record.html',locals())