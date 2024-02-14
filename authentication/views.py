from django.shortcuts import render

def signup(request):
    return render(request, 'authentication/signup.html')
    
def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return render(request, 'authentication/logout.html')