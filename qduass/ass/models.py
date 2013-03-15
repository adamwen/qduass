from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=700)
    openkey = models.CharField(max_length=700)

    accesstoken = models.CharField(max_lenght=700)
    expires_in = models.CharField(max_lenght=700)
    refresh_key = models.CharField(max_lenght=700)

    nickname = models.CharField(max_lenght=700)
    name = models.CharField(max_lenght=700)

