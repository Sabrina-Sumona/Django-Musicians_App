from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'my_app/index.html'
