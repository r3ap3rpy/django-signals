from django.urls import path
from . import views

urlpatterns = [
    path('sig/', views.index, name = 'sig')
]