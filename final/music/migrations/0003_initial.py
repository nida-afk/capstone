# Generated by Django 5.0.6 on 2024-06-29 12:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("music", "0002_delete_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("track_id", models.CharField(max_length=100, unique=True)),
                ("track_name", models.CharField(max_length=255)),
                ("artist_name", models.CharField(max_length=255)),
                ("collection_name", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
                ("artwork_url", models.URLField()),
                ("preview_url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="WatchList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "songs",
                    models.ManyToManyField(
                        related_name="watchlist_songs", to="music.song"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
