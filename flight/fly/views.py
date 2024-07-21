from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    for i in range (7):
        return HttpResponse("Hello ", i)
