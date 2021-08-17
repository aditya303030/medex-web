from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate 
from django.contrib import messages
from .models import DonationForm
from .forms import FormDonationForm    
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def homepage(request):
  return render(request,'home.html',{})

def about(request):
  return render(request,'about.html',{})

def whypage(request):
  return render(request,'whypage.html',{})

def donate(request):  
  donationform = FormDonationForm(request.POST or None)
  if donationform.is_valid():
    donationform.save()
  return render(request,'donate.html',context={'FormDonationForm':FormDonationForm})  