from django.urls import path
from . import views

# home app urls
urlpatterns = [
    path('', views.index, name='home')
]
