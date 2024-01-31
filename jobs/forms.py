from typing import Any
from django.forms import ModelForm
from .models import Job


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
