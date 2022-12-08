from users.models import Profile


def access_users(request):
    users = Profile.objects.filter_birthday()
    return {'users': users}
