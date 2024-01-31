from django.shortcuts import render
from jobs.models import Job, Category, Testimonials


def homepage(request):
    testimonials = Testimonials.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories, 'testimonials': testimonials})


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')


def testimonial(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials})
