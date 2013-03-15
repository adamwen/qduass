from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=70)
    openkey = models.CharField(max_length=70)

    accesstoken = models.CharField(max_lenght=70)
    expires_in = models.CharField(max_lenght=70)
    refresh_key = models.CharField(max_lenght=70)

    nickname = models.CharField(max_lenght=70)
    name = models.CharField(max_lenght=70)

