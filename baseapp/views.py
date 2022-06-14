from datetime import datetime
from django.shortcuts import redirect, render
from baseapp.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
# from anime_streaming_website.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail


def landing_page(request):
    return render(request, 'landing_page.html')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')