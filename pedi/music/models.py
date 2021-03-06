from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=500)

    def __str__(self):
        return "Album name is {0}, artist name is {1}".format(self.album_title, self.artist)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

