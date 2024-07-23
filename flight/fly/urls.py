from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:i>", views.flight, name = "fly"),
    path("sea", views.search, name = "search"),
]
