from django.urls import path

from . import views

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedBackView.as_view(), name='feedback'),
]
