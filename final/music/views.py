# music_player_app/views.py

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from .models import Song, User
from django.contrib.auth.decorators import login_required
from operator import itemgetter



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "music/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "music/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "music/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "music/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "music/register.html")



def index(request):
    if request.user.is_authenticated:
        return render(request, 'music/search.html')
    else:
        return HttpResponseRedirect(reverse("login"))

@login_required
def result(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artist_name')
        response = requests.get(f"https://itunes.apple.com/search?entity=musicTrack&limit=100&term={artist_name}")
        data = response.json()
        songs = data.get('results', [])
        return render(request, 'music/results.html', {'songs': songs})
    return render(request, 'music/search.html')

@login_required
def song_details(request, track_id):
     user= request.user
     response = requests.get(f"https://itunes.apple.com/lookup?id={track_id}")
     data = response.json()
     songs = data.get('results', [])[0]
     image = songs["artworkUrl100"].replace("100x100bb.jpg", "592x592bf.webp")
     date = songs["releaseDate"].split("T", 1)[0]


     song_exists = Song.objects.filter(track_id=track_id).exists()

     if not song_exists:

         ns = Song(track_id=songs.get('trackId'))
         ns.save()
     user_watchlist, created = Song.objects.get_or_create(track_id = track_id)
     w = user_watchlist.watchlist.filter(id=user.id).exists()

     return render(request, 'music/song_details.html', {'date': date,'song': songs, 'image': image, 'watch': w})

@login_required
def add(request, track_id):
    user_watchlist= Song.objects.get(track_id = track_id)
    user= request.user
    w = user_watchlist.watchlist.filter(id=user.id).exists()
    if w:
        user.watchlist.remove(user_watchlist)
    else:
        user.watchlist.add(user_watchlist)
    return redirect('watchlist')


@login_required
def watchlist(request):
    user = request.user
    songs = Song.objects.filter(watchlist=user)
    track_ids = [song.track_id for song in songs]
    music_data = []
    for track_id in track_ids:
        response = requests.get(f"https://itunes.apple.com/lookup?id={track_id}")
        data = response.json()
        if 'results' in data:
            music_data.append(data['results'][0])
    return render(request, 'music/watchlist.html', {'songs': music_data})

@login_required
def latest(request):
    popartists = ["taylor swift", "ed sheeran", "katy perry", "ellie goulding","rihanna",  "shawn mendes", "adele", "billie eilish" , "harry styles"]

    music_data = []

    for artist in popartists:
        response = requests.get(f"https://itunes.apple.com/search?media=music&entity=song&limit=10&term={artist}")
        data = response.json()

        if 'results' in data:
            songs = data.get('results', [])
            sort = sorted(songs, key=itemgetter('releaseDate'), reverse=True)
            music_data.extend(sort)

    return render(request, 'music/latest.html', {'sorted_songs': music_data})
