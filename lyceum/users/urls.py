from django.urls import path, re_path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('user_list/', views.user_list, name='user_list'),
    re_path(
        r'(?P<pk>[1-9]\d*)/$',
        views.user_detail,
        name='user_detail',
    ),
    path('profile', views.profile, name='profile'),
]
