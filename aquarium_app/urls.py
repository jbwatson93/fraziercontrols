from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/projects', views.ProjectView)
router.register("projects", views.ProjectView)
router.register("exhibits", views.ExhibitView)
router.register("projectexhibits", views.ProjectExhibitView)

urlpatterns = [path("", include(router.urls))]