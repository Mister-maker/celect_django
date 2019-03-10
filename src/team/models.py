from django.db import models

class Team(models.Model):
  Name = models.CharField(max_length=200)
  Post = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  linkedin = models.CharField(max_length=200)
  facebook = models.CharField(max_length=200)
  is_published = models.BooleanField(default=True)
  def __str__(self):
    return self.Name