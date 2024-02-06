from typing import Any
import os
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import LoginForm, EmployeeRegistrationForm, JobSeekerRegistrationForm, UpdateProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from jobs.models import JobApplication
from django.db.models import Q


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


@login_required()
def logout_user(request):
    logout(request)
    return redirect('accounts:login')


@login_required()
def profile(request, id):
    try:
        user = User.objects.get(id=id)
        profile = Profile.objects.get(user=user)
        return render(request, 'profile.html', {'profile': profile})
    except User.DoesNotExist:
        print("User Doesnot exist")

    except User.MultipleObjectsReturned:
        print("Multiple Objects Returned")
    except:
        print('Something went wrong.')


@login_required()
def view_resume(request, id):
    profile = get_object_or_404(Profile, id=id)
    file_path = profile.resume.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file, content_type='application/pdf')
            return response
    return render(request, '404.html')


def update_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(
            request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile', args=[id]))
    return render(request, 'update-profile.html', {'form': form})
