from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician, Album

# Create your views here.

def home(request):
    # return render(request, 'my_app/index.html', context=diction)
    # DJNGO query
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': "Live like a boss",'text_2':'This a list of Musicians', 'musician': musician_list}
    return render(request, 'my_app/index.html', context=diction)

def contact(request):
    diction = {}
    return render(request, 'my_app/contact.html', context=diction)

def about(request):
    diction = {}
    return render(request, 'my_app/about.html', context=diction)

# def index(request):
#     diction = {}
#     return render(request, 'my_app/index.html', context=diction)

# def index(request):
#     return HttpResponse("<h1>Hello World<h1>")

# def index(request):
#         return HttpResponse("<h1>MY app<h1>")

# def home(request):
#     return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")
#
# def contact(request):
#     return HttpResponse("<h1>This is Contact Page</h1> <a href='/my_app'>Homepage</a> <a href='/my_app/about/'>About</a>")
#
# def about(request):
#     return HttpResponse("<h1>About Us</h1> <a href='/my_app'>Homepage</a> <a href='/my_app/contact/'>Contact</a>")

# def home(request):
#     return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")
#
# def contact(request):
    # return HttpResponse("<h1>This is Contact Page</h1> <a href='/'>Homepage</a> <a href='/about/'>About</a>")
#
# def about(request):
#     return HttpResponse("<h1>About Us</h1> <a href='/'>Homepage</a> <a href='/contact/'>Contact</a>")
