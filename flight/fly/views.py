from django.shortcuts import render
from .models import Fly, Jun

# Create your views here.
def index(request):
    return (render(request, index.html, {
        
    }))
