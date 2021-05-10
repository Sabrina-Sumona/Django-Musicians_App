from django.conf.urls import url
from django.urls import path
from my_app import views

app_name = "my_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name='album_form'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('album_list/', views.album_list, name='album_list'),
    path('musician_list/', views.musician_list, name='musician_list'),
    path('musician_details/<int:artist_id>/', views.musician_details, name='musician_details'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_musician, name='delete_artist'),
]
