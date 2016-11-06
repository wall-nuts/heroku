from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from django.core.mail import send_mail
from first.models import Book
from django.http import HttpResponseRedirect
from first.forms import ContactForm

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

def display_meta(request):
    values = request.META.items()
    values = sorted(values,key = lambda x:x[0])
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))

def search(request):
    error = []
    if ('q' in request.GET):
        q = request.GET['q']
        if (not q):
            error.append('Enter a search tem.')
        elif len(q) > 20:
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_result.html',{'books':books,'query':q})
    return render_to_response('search_form.html', {'error': error})

def contact(request):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','xxxxxxxxx@qq.com'),
                ['wwwwwww@qq.com']
            )
            return HttpResponseRedirect('/contact_thanks/')
    else:
        form = ContactForm(initial={'subject':'主题'})
    return render(request,'contact_form.html',{'form':form})

def thanks(request):
    return render_to_response('contact_thanks.html')