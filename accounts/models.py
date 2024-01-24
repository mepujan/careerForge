from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ('job-seeker', 'Job Seeker'),
    ('employer', 'employer')
)

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('Others', 'Others')
)


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
                              'unique': 'User with that email already exist.'})
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    bio = models.TextField()
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.email} - user created."
