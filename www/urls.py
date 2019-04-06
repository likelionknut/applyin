from django.urls import path
from www import views


urlpatterns = [
    path('', views.index, name='index'),
]
