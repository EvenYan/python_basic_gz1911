from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request, 'index.html')
