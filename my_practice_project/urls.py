from django.contrib import admin
from django.urls import path
# from my_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', include('my_app.urls')),

    # path('index/', views.index, name='index'),
    # path('home/', views.index, name='index'),
    # path('', views.index, name='index'),

    # path('', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
]
