from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class CheckAudioName(models.Model):
    passUser = models.CharField(max_length=250)
    audioname = models.CharField(max_length=100)
    url_site = models.CharField(max_length=250)
    datetime = models.CharField(max_length=100)
    # video = EmbedVideoField(blank=True,verbose_name='Video')
