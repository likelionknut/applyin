from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from www.models import *


# Create your views here.

class Welcome(ListView):
    model = Job
    template_name = 'www/index.html'

# def index(request):
#     return render(request, 'www/index.html')


# def login(request):
#     return render(request, 'www/login.html')
