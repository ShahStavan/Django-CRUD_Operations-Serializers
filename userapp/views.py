from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def index(request):
    form = UserCreationForm()
    
