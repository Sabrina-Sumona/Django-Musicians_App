from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class Index(View):
    def get(self, request):
        return HttpResponse("Hello World!!")
