from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index, name='index'),
    # path('home/', views.index, name='index'),
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
