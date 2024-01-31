from typing import Any
from django.forms import ModelForm
from .models import Job, Testimonials


class SearchForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'category', 'location')


class PostJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('application_count', 'hiring_person', 'status')


class UpdateJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('application_count', 'hiring_person')


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonials
        exclude = ('user',)
