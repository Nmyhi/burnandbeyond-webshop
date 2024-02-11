from django.urls import path
from . import views

# profile app urls
urlpatterns = [
    path('', views.profile, name='profile')
]
