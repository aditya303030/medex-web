from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate 
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def register(request):
    if request.method =="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email= request.POST['email']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(password = password,username=username, first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print("Passwords don't match!!!")   
            messages.info(request,"Passwords don't match")
        return redirect('/')
    else:
        return render(request,'register.html',{})

def login(request):
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'User does not exist!')
            return redirect('login')
    else:
        return render(request, 'login.html',{})
    
def logout(request):
    auth.logout(request)
    return redirect('/login')
    
    # return render(request,'logout.html',{})
