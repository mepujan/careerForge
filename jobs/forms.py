from typing import Any
from django import forms
from django.forms import ModelForm
from .models import Job, Testimonials, JobApplication


class SearchForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'category', 'location')


class PostJobForm(ModelForm):
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Job
        exclude = ('application_count', 'hiring_person', 'status')


class UpdateJobForm(ModelForm):
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Job
        exclude = ('application_count', 'hiring_person')


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonials
        exclude = ('user',)


class ApplicationStatusForm(ModelForm):
    class Meta:
        model = JobApplication
        exclude = ('job', 'applicant')
