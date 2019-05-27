from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView
from www.models import *
from www.form import ApplicationForm

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

class Welcome(ListView):
    model = Job
    template_name = 'www/index.html'


class Apply(View):
    def get(self, request, apply_dest):
        application_form = ApplicationForm()
        return render(request, 'www/apply.html', {'application_form': application_form})

    def post(self, request, apply_dest):
        form_data = ApplicationForm(data=request.POST)
        if form_data.is_valid():
            application = form_data.save(commit=False)
            application.save()
        return redirect('index')

# def index(request):
#     return render(request, 'www/index.html')

def register(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confirmPass']:
            user = User.objects.create_user(
                username=request.POST['email'], password=request.POST['pass'], email=request.POST['name']
            )
            auth.login(request, user)
            return redirect('index')
        return render(request, 'www/register.html')

    return render(request,'www/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'www/login.html', {'error' : '이메일 혹은 패스워드가 맞지 않습니다.'})
    else:
        return render(request, 'www/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'www/index.html')
