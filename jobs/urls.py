from django.urls import path
from .views import JobListPageView,  job_detail_view, apply_job, my_jobs_list

app_name = 'jobs'

urlpatterns = [
    path('', JobListPageView.as_view(), name='job'),
    path('job/<int:id>/', job_detail_view, name='job-detail'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('myjobs/', my_jobs_list, name='my_jobs')
]
