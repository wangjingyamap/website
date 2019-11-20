from django.shortcuts import render
from django.views.generic import DetailView,TemplateView

# Create your views here.



class Coffee(TemplateView):
    # model=InstaUser
    template_name='coffee.html'
    
    # return render(request,'coffee.html')