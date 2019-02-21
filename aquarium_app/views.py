from django.shortcuts import render
from .models import Projects

# Create your views here.
def projectsIndex(request):
    context = {'projects': Projects.objects.all()}
    return render(request, 'aquarium_app/projectsIndex.html', context)