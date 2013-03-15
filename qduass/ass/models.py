from django.db import models

# Create your models here.
class User(models.Model):
	code = model.CharField(max_length=70)
	openid = model.CharField(max_length=70)
	openkey = model.CharField(max_length=70)

	accesstoken = model.CharField(max_lenght=70)
	expires_in = model.CharField(max_lenght=70)
	refresh_key = model.CharField(max_lenght=70)
