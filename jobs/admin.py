from django.contrib import admin
from django.utils.html import format_html
from .models import Job, Category, JobApplication, Testimonials

admin.site.site_header = "CareerForge"
admin.site.site_title = "CareerForge"
admin.site.index_title = "Welcome to CareerForge Admin Page"


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'deadline')
    search_fields = ('title', 'type', 'status')
    list_filter = ('title', 'type', 'status',)
    list_per_page = 20


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'status', 'job')
    list_filter = ('applicant', 'status')
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'i_class')
    list_filter = ('title',)
    list_per_page = 20


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')
    list_filter = ('user',)
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Testimonials, TestimonialAdmin)
