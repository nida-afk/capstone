from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()

    resp = f # Joining each entry with an HTML line break
    return HttpResponse(resp)

def flight(request, i):

    f = Fly.objects.get(pk=i)
    return render(request, "fly.html", {
            "fly" : f.name.all(),
            "f" : f
    } )


