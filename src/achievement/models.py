from django.db import models
from datetime import datetime


class Achievement(models.Model):
  title = models.CharField(max_length=50)
  short_description = models.CharField(max_length=150)
  home_page_description = models.TextField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  project_link = models.CharField(max_length=200)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  is_published = models.BooleanField(default=True)
  def __str__(self):
    return self.title
