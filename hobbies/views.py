from django.shortcuts import render

from django.views.generic import DetailView,TemplateView,ListView

# Create your views here.
from hobbies.models import Illstrations


class Illustrations(ListView):
    model=Illstrations
    template_name='illustrations.html'
    
