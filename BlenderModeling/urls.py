from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlenderModeling, name='Models')
]