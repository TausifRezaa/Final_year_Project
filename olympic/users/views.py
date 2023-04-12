from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def user_login(request):
    template_name = 'users/login.html'
    if  request.user.is_authenticated:
            return redirect('games_dashboard')
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('games_dashboard')
            
            else:
                messages.success(request, ("The login was failed."))
                return redirect('user_login')
            
    else:
        return render(request, template_name)
    

def user_register(request):
    template_name = 'users/register.html'

    if request.user.is_authenticated:
        return redirect('games_dashboard')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print('hait')
                messages.success(request, 'Account activated successfully')
                return redirect('user_login')
            else:
                print('valid vhaena')
        else:
            form = CustomUserCreationForm
    return render(request, template_name, {'form': form})