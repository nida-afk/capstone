from django.shortcuts import render
from .models import Fly, Jun
from django.http import HttpResponse

# Create your views here.
def index(request):
    f = Fly.objects.all()

    resp = [f"<li type =none> {d.id}  {d} </li>" for d in f] # Joining each entry with an HTML line break

    return HttpResponse(resp)
def flight(request, ids){
    f = f = Fly.objects.get(pk=ids)
    return render

}
