from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(username = request.POST['username'])
            return render (request,'signup.html', {'error':'Username is already taken!'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
            auth.login(request,user)
            return redirect('/login')
    else:
        return render(request, 'signup.html')  

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request, 'login.html') 

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user' : request.user})  
    else :
        return redirect('/login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html') 
    else :
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')