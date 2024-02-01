from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import LoginForm, EmployeeRegistrationForm, JobSeekerRegistrationForm


User = get_user_model()


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
                if user.role == 'employer':
                    return redirect('jobs:dashboard')
                else:
                    return redirect('/')
            messages.error(
                request, "Invalid username or password. Try Again...")

    return render(request, 'login.html', {'form': form})


class SignUpAsEmployee(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'signup.html'
    success_url = '/accounts/login'
    extra_content = {'title': 'Employer Registration'}

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        return render(request, 'signup.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_content'] = self.extra_content
        return context


class SignUpAsJobSeeker(CreateView):
    model = User
    form_class = JobSeekerRegistrationForm
    template_name = 'signup.html'
    success_url = '/accounts/login'
    extra_content = {'title': 'JobSeeker Registration'}

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        return render(request, 'signup.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_content'] = self.extra_content
        return context


def logout_user(request):
    logout(request)
    return redirect('accounts:login')


def profile(request, id):
    try:
        profile = User.objects.get(id=id)
        return render(request, 'profile.html', {'profile': profile})
    except User.DoesNotExist:
        print("User Doesnot exist")

    except User.MultipleObjectsReturned:
        print("Multiple Objects Returned")
    except:
        print('Something went wrong.')
