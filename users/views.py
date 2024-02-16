from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def loginUser(request):
    page = 'login'

    if request.is_authenticated:
        return redirect('products') 
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if request is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'username or password are incorrect')

    return render(request, 'users/login-register.html')

def registerUser(request):
    page = 'register'

    
    return render(request, 'users/login-register.html')

def logoutUser(request):
    return redirect('logout')

def profile(request, pk):
    return render(request, 'users/user-profile.html')

