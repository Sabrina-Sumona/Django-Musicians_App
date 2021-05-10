from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', include('my_app.urls')),
]
