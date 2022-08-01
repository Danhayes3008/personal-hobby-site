from django.urls import path

from . import views

urlpatterns = [
    path('', views.Electronics, name='Electronics')
]