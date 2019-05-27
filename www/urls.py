from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from www.views import *

urlpatterns = [
    path('', Welcome.as_view(), name='index'),
    # path('login/', views.login, name='login'),
]
