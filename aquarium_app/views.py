from django.shortcuts import render
from rest_framework import viewsets
from .models import Projects, Exhibits, ProjectExhibits, Items
from .serializers import *

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ExhibitView(viewsets.ModelViewSet):
    queryset = Exhibits.objects.all()
    serializer_class = ExhibitsSerializer

class ProjectExhibitView(viewsets.ModelViewSet):
    queryset = ProjectExhibits.objects.all()
    serializer_class = ProjectExhibitsSerializer

class ItemsView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer