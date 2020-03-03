from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static

def home(request):

    context = {

    }

    return render(request, 'index.html', context)
