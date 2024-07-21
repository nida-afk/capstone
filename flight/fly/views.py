from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    response_text = ""
    for i in range(0, 7):
        response_text += f"Hello {i} "
    return HttpResponse(response_text)
