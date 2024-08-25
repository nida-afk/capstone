# Objectives
Becoming more comfortable with Django.
Gain experience with web development design.
Completing the final project of CS50W !

# Feel free to visit my project repository here
# [https://github.com/nida-afk/capstone/](https://github.com/nida-afk/capstone/)
## [demo video](https://youtu.be/nNIZtJGTH-A?si=A281ROqxWBbJhpm6)
# Deployed On
# [https://capstone-e0i1.onrender.com](https://capstone-e0i1.onrender.com)
## Overview
In this project, I have build a web application for audio streaming "Amusify" similar to spotify or itunes . Users will be able to search the songs menu, add songs to their playlists, and download their songs.
It gives instant access to vast variety of songs. An online library of songs, music tracks and podcasts.

# **Distinctiveness and Complexity**:
API Calls:
My app relies on external services / API  (iTunes API) for data retrieval.
Properly handling API calls and rechecking the data retrieved , processing it and formatting it to be displayed to the user is crucial.
My app interacts with itunes to fetch real-time music data using python and log the track_ids into the data base .
*PlayList and User-Specific Data*:
A user can add and remove songs from playlists just by the track_id .
The app retrieves and displays personalized playlistss for each logged-in user.
Iterating over track IDs and making API requests.
*latest songs*:
This function retrieves and sorts songs from specific artists This is where complexity gets even more complex!
It queries the iTunes  for songs related to artists like Taylor Swift, Ed Sheeran, etc.
The latest songs by each artist is displayed first.
UI:
in latest.html Displaying the songs and letting the songs overflow horizontally
each row containing 10 songs . wrapping the songs , using card layouts was complex for me.
Using javascipt to handle the overflow of songs when the user hovers over the specific song row but not to interfere wiht the other UI components like other song rows.

# What each file in my final project contains:
**Views.py**:
Contains all the views (app logic) of the Amusify application. contians functions:
Has login , logout , register views to handle the authentication of the user .

index page:
This function checks if the user is authenticated (logged in). If so, Allows user to search for songs. Otherwise, it redirects the user to the login page.

result(request):
It uses the artist_name parameter from the POST request.
appends that to the URL to search for music tracks related to that artist.
After that response is passed to the 'music/results.html' template for rendering.

song_details(request, track_id):
This function retrieves details about a specific song based on its track_id from itunes.
The song’s release date and artwork URL are extracted from the API response.
It checks if the song id exists in the database. If not, it creates a new Song object by just logging in the track_id.
renders songs_details.

add(request, track_id):
Allows user to add or remove the song from their playlists.
It retrieves the track_id and the current user, checks the current state if the song is already in playlists.
loads or renders watchlist.html directly.

watchlist(request):
This function displays the user’s playlists.
 It retrieves all the track_id from the playlist for each song, it fetches additional details from the iTunes API.

latest(request):
Sorts the songs and displays latest songs from popular artists.
renders 'music/latest.html' template.

Models.py:
All the app data or storage for this application has 2 models User, Song .
Song: has 2 fields viz:
track_id : logs all the ids of visited songs.
watchlist : many to many relation between user and song.

In my templates folder i have all the html templates which corresponds with my urls.py

search.js :
Genrally handles the UI for two files :
1) search form  which displays suggestions based on the value entered in the input field.
2) latest to allow horizontal scrolling for the artist component which is hovered on.


## Running the application :
in your terminal run $ cd itune/final command.
After entering into the final directory.
Run python manage.py runserver
View the project !
There are no additional requirements or no additional packages to be installed be free to use.


