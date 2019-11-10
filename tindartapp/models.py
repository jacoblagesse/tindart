from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Art(models.Model):
	user = models.CharField(max_length=200, unique=True)
	artwork = models.ImageField(upload_to='images/', null=True)