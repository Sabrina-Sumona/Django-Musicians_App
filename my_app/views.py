from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from my_app.models import Musician, Album

# Create your views here.

class Index(ListView):
    context_object_name = 'musician_list'
    model = Musician
    template_name = 'my_app/index.html'

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = Musician
    template_name = 'my_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name','last_name','instrument')
    model = Musician
    # django automatically creates this template_name, but also can give it to avoid any unexpectations
    template_name = 'my_app/musician_form.html'
