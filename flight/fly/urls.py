from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:ids>", views.flight, name = "fly"),

]
