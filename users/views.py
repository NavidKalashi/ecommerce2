from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, ProfileForm
from .models import Profile

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
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

    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('edit-account')
        else:
            return redirect('profiles')
        
    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# def profile(request, pk):
#     profile = Profile.objects.get(id=pk)
#     context = {'profile': profile}
#     return render(request, 'users/user-profile.html', context)

def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'users/profile-form.html', context)