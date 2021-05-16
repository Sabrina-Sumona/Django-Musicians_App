from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView
from my_app.models import Musician, Album

# Create your views here.

class Index(ListView):
    context_object_name = 'musician_list'
    model = Musician
    template_name = 'my_app/index.html'
