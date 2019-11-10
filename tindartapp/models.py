from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid

class Art(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=200)
    artwork = models.ImageField(upload_to='images/', null=True)
    likes = models.IntegerField(null=True, default=0)
    dislikes = models.IntegerField(null=True, default=0)

    def get_absolute_url(self):
        return ('/main/%s/' % str(self.id))