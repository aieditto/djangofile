from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')