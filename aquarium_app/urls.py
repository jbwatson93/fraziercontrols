from django.urls import path
from . import views

urlpatterns = [
   path('', views.projectsIndex, name='projectsIndex')
]