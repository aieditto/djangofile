from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def service(request):
    return HttpResponse('From Service')

def profile(request):
    return HttpResponse('From profile')