from django.db import models

class RegistrationForm(models.Model):
    student_name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    linkedin_url = models.CharField(max_length=200, blank=True)
    github_url = models.CharField(max_length=200, blank=True)
    portfolio_url = models.CharField(max_length=200, blank=True)
    date_of_birth = models.CharField(max_length=100)
    resume = models.CharField(max_length=200, blank=True)
    college_company_name = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    internship_details = models.TextField(blank=True)
    def __str__(self):
        return self.student_name