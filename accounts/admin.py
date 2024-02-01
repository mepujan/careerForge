from django.contrib import admin
from .models import User, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
