from django.shortcuts import render
from jobs.models import Job


def homepage(request):
    featured_jobs = Job.objects.filter(featured_job=True)
    return render(request, 'homepage.html', {'jobs': featured_jobs})


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')
