from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.first_name
    

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.PositiveSmallIntegerField()
    artiste_id = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.title

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.CharField(max_length=2000)
    song_id = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.Song.title