from django.urls import path
from .views import login_user, signup, logout_user

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout')
]
