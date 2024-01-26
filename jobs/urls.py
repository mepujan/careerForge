from django.urls import path
from .views import JobListPageView,  job_detail_view

app_name = 'jobs'

urlpatterns = [
    path('', JobListPageView.as_view(), name='job'),
    path('job/<int:id>/', job_detail_view, name='job-detail')
]
