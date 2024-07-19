from django.shortcuts import render

# Create your views here.
# accounts/views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    