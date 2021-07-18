from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Medicinehompage
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
  