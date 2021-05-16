from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'my_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_text_1'] = 'Sample Text 1'
        context['sample_text_2'] = 'Sample Text 2'
        return context
