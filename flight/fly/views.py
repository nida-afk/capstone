from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()

    return render(request, "index.html", {
        "f" : f

    })

def flight(request, i):

    f = Fly.objects.get(pk=i)
    return render(request, "fly.html", {
            "fly" : f.name.all(),
            "f" : f
    } )


