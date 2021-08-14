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
# Create your views here.

def homepage(request):
  return render(request,'home.html',{})

def about(request):
  return render(request,'about.html',{})

def whypage(request):
  return render(request,'whypage.html',{})
#Not working yet
def donate(request):
  if request.method=="POST":
    # if request.POST.get('Name') and request.POST.get('email') and request.POST.get('search_medicine') and request.POST.get('quantity') and request.POST.get('picture') and request.POST.get('expirydate') and request.POST.get('address'):    
      # donation_record = DonationForm()
    Name = request.POST['Name']
    email = request.POST['email']
    search_medicine = request.POST['search_medicine']
    quantity = request.POST['quantity']
    picture = request.POST['picture']
    expirydate = request.POST['expirydate']
    address = request.POST['address']
    donation_record = User.objects.create_user(Name=Name,email=email,search_medicine=search_medicine,quantity=quantity,picture=picture,expirydate=expirydate,address=address)
    donation_record.save()
    messages.info(request,'Record Saved successfully')
    print('donation record saved!!!')
    return redirect('/')
  else:
    return render(request,'donate.html',{})
  return render(request,'donate.html',{})