from django.conf.urls import url
from django.urls import path
from my_app import views

urlpatterns = [
    # path('', views.index, name='index'),

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
