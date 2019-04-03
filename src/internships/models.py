from django.db import models
from datetime import datetime

class Internship(models.Model):
  full_name = models.CharField(max_length=200)
  roll_number = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  company_name = models.CharField(max_length=200)
  internship_profile = models.CharField(max_length=200)
  internship_duration = models.CharField(max_length=200)
  internship_details = models.CharField(max_length=200)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  is_published = models.BooleanField(default=True)
  def __str__(self):
    return self.full_name
