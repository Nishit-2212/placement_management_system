from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class users_data(models.Model):
#     full_name = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to='images')
#     dob = models.DateField()
#     degree = models.CharField(max_length=30)



class Student(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null = True , blank = True)
    name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='profile_pic/',null=True)
    contact_no = models.CharField(max_length=100)
    dob = models.DateField()
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()

# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     industry = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
#
# class JobProfile(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     required_skills = models.TextField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#
# class Placement(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
#     placement_date = models.DateTimeField(auto_now_add=True)
#
# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     description = models.TextField()
