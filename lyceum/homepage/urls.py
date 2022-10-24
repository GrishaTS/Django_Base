from django.urls import path

from . import views

app_name = 'homapage'
urlpatterns = [
    path('', views.home, name='home')
]
