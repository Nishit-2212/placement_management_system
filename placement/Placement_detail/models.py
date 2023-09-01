from django.db import models

# Create your models here.

class Placement(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
    placement_date = models.DateTimeField(auto_now_add=True)