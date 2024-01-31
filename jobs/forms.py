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
        exclude = ('application_count', 'hiring_person')

    def save(self, commit: bool = True) -> Any:

        job = super().save(commit=False)
        job.hiring_person = self.request.user.id
        if commit:
            job.save()
        return job
