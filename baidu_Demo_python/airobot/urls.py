from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'airobot'

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),  # Add this line for the chat endpoint
]