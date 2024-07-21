from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    resp = ""
    f = Fly.objects.all()
    for d in f:
        resp += "\n"
        resp += f" {d} "
        resp += f"{d.id}"

    return HttpResponse(resp)
