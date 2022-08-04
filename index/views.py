from multiprocessing import context
from django.shortcuts import render
from BlenderModeling.models import blenderModels
from settings.settings import MEDIA_ROOT, MEDIA_URLS

# Create your views here.
def Index(request):
    models = blenderModels.objects.all()
    context = {
        "models": models
    }
    return render(request, 'index.html', context)