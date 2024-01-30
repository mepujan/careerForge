from django.forms import ModelForm
from .models import Job


class SearchForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'category', 'location')
