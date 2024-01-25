from django.contrib.auth import get_user_model

User = get_user_model()


def profile_pic(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        return {'profile_pic': profile.profile_pic}
    return {}
