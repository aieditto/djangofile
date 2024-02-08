from django.http import HttpResponse

def profile(request):
    return HttpResponse('Wellcome to Company profile ')
def contact(request):
    return HttpResponse('Zero One Eight  is a company that offers consulting services in the field of IT and Cybersecurity')