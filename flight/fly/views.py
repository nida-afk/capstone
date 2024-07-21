from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    for i in range(0,7):
        name = "nida"
        n +=  HttpResponse(f"Hello {i}" )
    return n
