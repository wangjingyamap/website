from django.shortcuts import render

from django.views.generic import DetailView,TemplateView,ListView

# Create your views here.
from hobbies.models import Illustrations,Post,Photographies


class IllustrationsView(ListView):
    model=Illustrations
    template_name='illustrations.html'
    

class IllustrationsDetails(DetailView):
    model=Illustrations
    template_name='illustrations_details.html'
    


class Photography(ListView):
    model=Post
    template_name='photography.html'
    

class PhotographyDetails(DetailView):
    model=Post
    template_name='photography_details.html'
    
