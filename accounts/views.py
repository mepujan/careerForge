from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def login_user(request):
    if (request.user.is_authenticated):
        return redirect('homepage')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            messages.error(
                request, "Invalid username or password. Try Again...")

    return render(request, 'login.html', {'form': form})


def signup(request):
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
