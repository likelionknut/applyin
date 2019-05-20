from django.shortcuts import render, HttpResponseRedirect


# Create your views here.

def index(request):
    # return HttpResponseRedirect('/login')
    return render(request, 'www/index.html')


def login(request):
    return render(request, 'www/login.html')
