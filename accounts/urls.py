from django.urls import path
from .views import login_user, SignUpAsJobSeeker, logout_user, SignUpAsEmployee, profile, view_resume

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('employee-signup/', SignUpAsEmployee.as_view(), name='signup-employer'),
    path('jobseeker-signup/', SignUpAsJobSeeker.as_view(), name='signup-employee'),
    path('profile/<int:id>/', profile, name='profile'),
    path('view-resume/<int:id>/', view_resume, name='view-resume')
]
