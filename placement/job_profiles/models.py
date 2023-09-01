from django.db import models

# Create your models here.
class JobProfile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.TextField()
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
