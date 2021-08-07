from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Medicinehompage
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate 
from django.contrib import messages
# Create your views here.

def homepage(request):
  medicineform = Medicinehompage()
  if request.method=="POST":
    medicineform = Medicinehompage(request.POST)
    if medicineform.is_valid():
      medicineform.save()
      print('Entry Created')
      return redirect('/')
  context ={
    "medicineform":medicineform
  }
  return render(request,'home.html',context)

def about(request):
  return render(request,'about.html',{})

def whypage(request):
  return render(request,'whypage.html',{})
  
def donate(request):
  return render(request,'donate.html',{})