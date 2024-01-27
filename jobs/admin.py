from django.contrib import admin
from .models import Job, Category, JobApplication

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(JobApplication)
