from django.shortcuts import render

# Create your views here.
def contact(request):
    return render (request,'first_app/index.html' ,
                   context={'Name':'Anis',
                            'Expertise': 'Graphics Deisgn', 'tk': 2567})