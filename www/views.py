from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView
from www.models import *
from www.form import ApplicationForm


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


# def login(request):
#     return render(request, 'www/login.html')
