from django.db import models
from django.contrib.auth.models import User
import datetime


class University(models.Model):
    name = models.CharField(max_length=100)
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='mainapp/question_images/')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.datetime.now)
    

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='mainapp/question_images/')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.datetime.now())




# class Project(models.Model):
#     pass

# class Referral_request(models.Model):
#     from_user = models.ForeignKey(Student)
#     to_user = models.ForeignKey(Student)
#     refer_requested = models.ForeignKey(Referral)

