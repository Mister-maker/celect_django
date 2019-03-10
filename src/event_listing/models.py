from django.db import models
from datetime import datetime

class Event(models.Model):
  title = models.CharField(max_length=200)
  place = models.CharField(max_length=200)
  google_form_link = models.CharField(max_length=500)
  google_map_link = models.CharField(max_length=500)
  description = models.TextField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title