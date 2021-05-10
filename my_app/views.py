from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician, Album

from my_app.form import MusicianForm
from my_app.form import AlbumForm
# Create your views here.

def index(request):
    diction = {'title':"Home Page", 'text':"Music "}
    return render(request,'my_app/index.html', context=diction )

def musician_list(request):
    musician_list = Musician.objects.all()
    diction = {'title':"List of Musicians", 'text':'List of Musicians:', 'musician_list':musician_list}
    return render(request, 'my_app/musician_list.html', context=diction)

def album_list(request):
    album_list = Album.objects.all()
    diction = {'title':"List of Albums", 'text':'List of Albums:', 'album_list':album_list}
    return render(request, 'my_app/album_list.html', context=diction)

def musician_form(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':"Add Musician", 'text':'Add Musician', 'musician_form':MusicianForm() }
    return render(request, 'my_app/musician_form.html', context=diction)

def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':"Add Album" , 'text':'Add Album','album_form':AlbumForm()}
    return render(request, 'my_app/album_form.html',context=diction)
