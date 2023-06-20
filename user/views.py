from django.shortcuts import render,redirect, HttpResponse
from .forms import UserRegistration, UserProfiling
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    form = UserRegistration()
    if request.method == 'POST':
        form  = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User Created!")
            person = login(request, user)
            return redirect('profile')
        
    context = {
        'form': form
    }
    
    return render(request,  'user/register.html', context)


@login_required(login_url='login')
def profiling(request):
    profile = UserProfiling()
    if request.method == 'POST':
        profile = UserProfiling(request.POST)
        if profile.is_valid():
            form = profile.save(commit=False)
            form.user_profile = request.user
            form.save()
            return HttpResponse('Profile Updated')  
        
    context = {
        'profile': profile
    }
    
    return render(request, 'user/profilin.html', context)


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        passcode = request.POST['passcode']
        check = authenticate(request, username = username, password = passcode)
        # logged = False
        
        if check is not None:
            login(request, check)  
            return redirect('journal')
        
    return render(request, 'user/login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')