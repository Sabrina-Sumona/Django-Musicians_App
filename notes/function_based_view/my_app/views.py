from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician, Album

from my_app.form import MusicianForm
from my_app.form import AlbumForm

from django.db.models import Avg

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

def musician_details(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title':"Musician Details", 'artist_info':artist_info, 'album_list':album_list, 'artist_rating':artist_rating}
    return render(request, 'my_app/musician_details.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return musician_details(request, artist_id)

    diction = {'edit_form':form}
    return render(request, 'my_app/edit_artist.html', context=diction)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album_info)
    diction = {}
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!'})

    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request,'my_app/edit_album.html', context=diction)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success':'Album Deleted Successfully!'}
    return render(request, 'my_app/delete.html', context=diction)

def delete_musician(request, artist_id):
    artist = Musician.objects.get(pk=artist_id).delete(0)
    diction = {'delete_success':'Musician Deleted Successfully!'}
    return render(request, 'my_app/delete.html', context=diction)
