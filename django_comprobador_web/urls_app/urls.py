from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesar_url, name='procesar_url'),
]