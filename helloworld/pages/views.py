from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World!")
