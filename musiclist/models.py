from django.db import models

class songitem(models.Model):
    songname = models.TextField()
    artist = models.TextField()
    votes = models.IntegerField()
