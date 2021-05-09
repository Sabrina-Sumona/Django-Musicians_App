from django.conf.urls import url
from django.urls import path
from my_app import views

app_name = "my_app"

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
]
