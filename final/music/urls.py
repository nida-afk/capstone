# music_player_app/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('result/', views.result, name='result'),
    path('song/<int:track_id>/', views.song_details, name='song_details'),
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('latest',views.latest, name = 'latest'),
    path('add/<int:track_id>/', views.add, name='add'),


]
