from django.views.generic import ListView
from .models import Job

# Create your views here.


class JobListPageView(ListView):
    model = Job
    queryset = Job.objects.all()
    template_name = 'jobs-list.html'
    context_object_name = 'jobs'
