from django.shortcuts import render

from django.views.generic import DetailView,TemplateView,ListView

# Create your views here.
from hobbies.models import Illustrations


class Illustrations(ListView):
    model=Illustrations
    template_name='illustrations.html'
    

class IllustrationsDetails(DetailView):
    model=Illustrations
    template_name='illustrations_details.html'
    


