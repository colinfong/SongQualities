from django.db import models

class Songs(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=20)
    quality = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=10)

class Token(models.Model):
    user = models.CharField(unique = True, max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    access_token = models.CharField(max_length = 500)
    refresh_token = models.CharField(max_length = 500)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length = 50)