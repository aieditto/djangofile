from django.http import HttpResponse

def about(request):
    return HttpResponse('Tum  kon ho?')
def paisa(request):
    return HttpResponse('Paisa Dedere Baba')