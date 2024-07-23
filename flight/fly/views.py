from django.shortcuts import render
from .models import Fly, Jun, Name
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()

    return render(request, "index.html", {
        "fi" : f

    })

def flight(request, i):

    f = Fly.objects.get(pk=i)
    return render(request, "fly.html", {
            "fly" : f.name.all(),
            "f" : f
    } )
def search(request):
    if request.method == 'POST':
        s = request.POST["query"]
        for i in Jun.objects.all():
            if s == i.name:
                j = Jun.objects.get(name = s)
                d = j.forest.all()
        return render(request, "search.html", {
        "data" : d
    })
    else:
        d = []
        return render(request, "search.html", {
        "data" : d
    })
