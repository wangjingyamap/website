from django.shortcuts import render

from django.views.generic import DetailView,TemplateView,ListView

# Create your views here.
from hobbies.models import illustrations


class Illustrations(ListView):
    model=illustrations
    template_name='illustrations.html'
    

class IllustrationsDetails(DetailView):
    model=illustrations
    template_name='illustrations_details.html'
    


