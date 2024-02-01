from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(
        label='password', max_length=200, widget=forms.PasswordInput())


class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1',
                  'password2', 'gender', 'bio', 'address', 'mobile', 'profile_pic')

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.role = 'employer'
        if commit:
            user.save()
        return user


class JobSeekerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1',
                  'password2', 'gender', 'bio', 'address', 'mobile', 'profile_pic')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'job-seeker'
        if commit:
            user.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    experience = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    skill = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Profile
        exclude = ('user',)
