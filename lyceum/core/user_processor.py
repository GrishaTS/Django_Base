from users.models import Profile


def access_users(request):
    users = Profile.objects.published()
    return {'users': users}
