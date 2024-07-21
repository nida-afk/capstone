from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()
    resp = ([f"<li>  {d.id}  {d} <li>" for d in f])  # Joining each entry with an HTML line break

    return HttpResponse(resp)
