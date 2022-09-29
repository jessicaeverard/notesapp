from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError

def createaccount(request):
    if request.method == 'GET':
        return render(request, 'createaccount.html', 
                       {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], 
                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'createaccount.html', 
                 {'form':UserCreateForm,
                 'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'createaccount.html', 
             {'form':UserCreateForm, 'error':'Passwords do not match'})

def logoutaccount(request):        
    logout(request)
    return redirect('loginaccount')

def loginaccount(request):    
    if request.method == 'GET':
        return render(request, 'login.html', 
                      {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'login.html', 
                    {'form': AuthenticationForm(), 
                    'error': 'username and password do not match'})
        else: 
            login(request,user)
            return redirect('index')
