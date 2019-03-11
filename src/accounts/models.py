from django.db import models

class RegistrationForm(models.Model):
    text = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name