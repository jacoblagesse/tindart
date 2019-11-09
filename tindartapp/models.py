from django.db import models
from PIL import Image

class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username

class Artist(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username

class Art(models.Model):
	artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='artwork', max_length=200, null=True)
	artwork = models.ImageField(upload_to='images/', null=True)