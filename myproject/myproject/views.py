from django.shortcuts import render
from django.htpp import HttpResponse

def home(request):
    template_name = 'home.html'
    context = {
        'title' :'my home',
        'welcome': 'welcome my home',
    }
    return render(request, template_name, context)