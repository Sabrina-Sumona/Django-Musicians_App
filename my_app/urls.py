from django.conf.urls import url
from django.urls import path
from my_app import views

app_name = "my_app"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
]
