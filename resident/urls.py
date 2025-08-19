from django.urls import path
from . import views

urlpatterns = [
    path('add/house', views.add_house, name='add_house'),
]
