from django.shortcuts import render
from rest_framework import viewsets
from .models import Projects
from .serializers import *

# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
