from django.db import models
from django.contrib.auth.models import AbstractUser
from abstract.base import BaseModel
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField


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
    role = models.CharField(
        max_length=10, default='job-seeker', choices=USER_TYPE)
    profile_pic = models.ImageField(
        upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return f"{self.email} - user created."

    @property
    def job_applied(self):
        return self.applicant.all()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def validete_file_size(value):
    max_size = 5*1024*1024
    if value.size > max_size:
        raise ValidationError('File size mustnot exceed 5MB.')


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = RichTextField()
    skill = RichTextField()
    github_url = models.URLField(null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to='resume', validators=[
                              FileExtensionValidator(['pdf', 'docx']), validete_file_size])

    def __str__(self):
        return f"{self.user.username} profile created"

    class Meta:
        ordering = ('-updated',)
