from django.urls import path
from . import views

urlpatterns=[
    path('service/',views.service),
    path('profile/',views.profile)
]