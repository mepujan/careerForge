from django.urls import path
from .views import JobListPageView

app_name = 'jobs'

urlpatterns = [
    path('', JobListPageView.as_view(), name='job')
]
