from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from www.views import *

urlpatterns = [
    path('', Welcome.as_view(), name='index'),
    path('apply/<int:apply_dest>/', Apply.as_view(), name='apply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
