from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime
from .models import Job, JobApplication, Testimonials
from .forms import SearchForm, PostJobForm, UpdateJobForm, TestimonialForm


User = get_user_model()
# Create your views here.


class JobListPageView(ListView):
    model = Job
    template_name = 'job-list.html'
    context_object_name = 'jobs'
    # paginate_by = 3

    def get_queryset(self):
        qs = Job.objects.filter(Q(status='active') and Q(
            deadline__gt=datetime.now()))
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Available Jobs'
        return context


def job_detail_view(request, id):
    job = get_object_or_404(Job, id=id)
    already_applied = False
    if request.user.is_authenticated:
        jobs_ = JobApplication.objects.select_related(
            'job').filter(applicant=request.user)
        for job_ in jobs_:
            if job == job_.job:
                already_applied = True
                break
    return render(request, 'job-detail.html', {'job': job, 'applied': already_applied})


@login_required(login_url='/accounts/login')
def apply_job(request, job_id):
    try:
        job_ = get_object_or_404(Job, id=job_id)
        JobApplication.objects.create(
            applicant=request.user, job=job_)
        job_.application_count += 1
        job_.save()
        messages.success(request, "Job Applied.")
    except:
        messages.error(request, 'Something went wrong. Try Again later...')
    return redirect('jobs:job-detail', id=job_id)


@login_required(login_url='/accounts/login')
def my_jobs_list(request):
    jobs_applied = JobApplication.objects.select_related(
        'job').filter(applicant=request.user)
    jobs = []

    for job_ in jobs_applied:
        jobs.append(job_.job)
    return render(request, 'job-list.html', {'jobs': jobs, 'title': 'My Jobs'})


def search_job(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            location = form.cleaned_data.get('location')
            jobs = Job.objects.filter(Q(title__icontains=title), Q(category=category), Q(location__icontains=location), Q(status='active'), Q(
                deadline__gt=datetime.now()))
            return render(request, 'index.html', {'jobs': jobs})
        messages.error(request, 'Something went wrong. Try Again')
    return render(request, 'index.html')


class CreateJob(LoginRequiredMixin, CreateView):
    model = Job
    form_class = PostJobForm
    template_name = 'post-job.html'
    context_object_name = 'form'
    success_url = reverse_lazy('jobs:myjobs')

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, files=self.request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hiring_person = self.request.user
            instance.save()
            return redirect('jobs:my_jobs')
        return render(request, 'post-job.html', {'form': form})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Job'
        context['btn_name'] = 'Create'
        return context


class UpdateJob(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = UpdateJobForm
    template_name = 'post-job.html'
    context_object_name = 'form'
    success_url = reverse_lazy('jobs:myjobs')

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, files=self.request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hiring_person = self.request.user
            instance.save()
            return redirect('jobs:my_jobs')
        return render(request, 'post-job.html', {'form': form})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Job Information'
        context['btn_name'] = 'Update'
        return context


@login_required()
def delete_job(request, id):
    get_object_or_404(Job, id=id).delete()
    messages.success(request, 'Job Deleted Successfully')
    return redirect('jobs:job-posted')


class ViewMyJobPosted(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job-list.html'
    context_object_name = 'jobs'
    # paginate_by = 3

    def get_queryset(self):
        qs = Job.objects.filter(hiring_person=self.request.user)
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Jobs Posted'
        return context


class PostTesimonials(LoginRequiredMixin, CreateView):
    model = Testimonials
    form_class = TestimonialForm
    success_url = 'testimonial'
    template_name = 'testimonial-form.html'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(self.request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            return redirect('testimonial')
        return render(request, 'testimonial-form.html', {'form': form})


class ApplicantListPageView(ListView):
    model = Job
    template_name = 'applicant-list.html'
    context_object_name = 'applicants'
    # paginate_by = 3

    def get_queryset(self):
        qs = get_object_or_404(Job, id=self.kwargs.get('pk'))
        return qs
