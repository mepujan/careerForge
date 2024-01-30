from django.shortcuts import render
from jobs.models import Job


def homepage(request):
    featured_jobs = Job.objects.filter(featured_job=True)
    return render(request, 'index.html', {'jobs': featured_jobs})


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')


def testimonial(request):
    return render(request, 'testimonial.html')
