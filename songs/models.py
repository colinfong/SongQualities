from django.db import models

class Songs(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=20)
    quality = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=10)

