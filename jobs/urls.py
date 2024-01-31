from django.urls import path, include
from .views import (JobListPageView,  job_detail_view, apply_job, my_jobs_list, search_job,
                    CreateJob, ViewMyJobPosted, delete_job, UpdateJob, PostTesimonials)
from src.views import homepage
app_name = 'jobs'

urlpatterns = [
    path('', JobListPageView.as_view(), name='job'),
    path('job/<int:id>/', job_detail_view, name='job-detail'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('myjobs/', my_jobs_list, name='my_jobs'),
    path('search/', search_job, name='search_job'),
    path('create-testimonial/', PostTesimonials.as_view(),
         name='create-testimonial'),
    path('employer/dashboard/',
         include(
             [
                 path('', homepage, name='dashboard'),
                 path('post-job', CreateJob.as_view(), name='post-job'),
                 path('my-jobs', ViewMyJobPosted.as_view(), name='job-posted'),
                 path('delete-job/<int:id>/', delete_job, name='delete-job'),
                 path('update-job/<int:pk>/',
                      UpdateJob.as_view(), name='update-job')
             ]
         )
         ),
    path('new-job/', CreateJob.as_view(), name='create-job')
]
