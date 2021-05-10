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
]
