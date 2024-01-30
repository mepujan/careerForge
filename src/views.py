from django.shortcuts import render
from jobs.models import Job, Category


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')


def testimonial(request):
    return render(request, 'testimonial.html')
