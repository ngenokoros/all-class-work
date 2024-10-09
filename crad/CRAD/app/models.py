from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length=100)
    adm_no = models.IntegerField(max_length=100)
    age = models.IntegerField(max_length=100)
    email=models.CharField(blank=True, null= False , max_length=100)
    image = models.ImageField(upload_to = 'images/',default='default.jpg')
