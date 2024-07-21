from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()
    resp = "\n".join([f" {d} {d.id}" for d in f])  # Joining each entry with a new line

    return HttpResponse(resp)
