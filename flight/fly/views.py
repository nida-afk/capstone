from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    response_text = ""
    f = Fly.objects.all()
    for d in f:

        response_text += f" {'\n'} + {d}"
    return HttpResponse(response_text)
