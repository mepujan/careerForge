from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from datetime import date
from .models import Job


# Create your views here.


class JobListPageView(ListView):
    model = Job
    template_name = 'jobs-list.html'
    context_object_name = 'jobs'
    # paginate_by = 3

    def get_queryset(self):
        qs = Job.objects.filter(Q(status='active'))
        return qs


def job_detail_view(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'job-details.html', {'job': job})
