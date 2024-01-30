from django.contrib import admin
from .models import Job, Category, JobApplication

admin.site.site_header = "CareerForge"
admin.site.site_title = "CareerForge"
admin.site.index_title = "Welcome to CareerForge Admin Page"

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(JobApplication)
