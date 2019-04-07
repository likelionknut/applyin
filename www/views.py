from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'www/index.html')


def login(request):
    return render(request, 'www/login.html')
