from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from my_app.models import Musician, Album
from django.urls import reverse_lazy

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

class UpdateMusician(UpdateView):
    fields = ('first_name','last_name', 'instrument')
    model = Musician
    template_name = 'my_app/musician_form.html'

class DeletMusician(DeleteView):
    context_object_name = 'musician'
    model = Musician
    # if Successfully deleted
    success_url = reverse_lazy("my_app:index")
    template_name = 'my_app/delete_musician.html'
