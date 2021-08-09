from django.urls import path

from . import views

app_name = 'quacks'

urlpatterns = [
    path('feed/', views.feed, name='quacks'),
]