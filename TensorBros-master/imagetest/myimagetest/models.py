from __future__ import unicode_literals

from django.db import models

# Create your models here.

def upload_location(name,filename):
    return "%s" % (filename)

class VideoModel(models.Model):
	primary_key = models.AutoField(primary_key=True)
	video = models.FileField(upload_to=upload_location)