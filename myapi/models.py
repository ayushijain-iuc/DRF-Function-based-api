from django.db import models

class Book(models.Model):
    name=models.CharField(max_length=10)
    rollno=models.IntegerField()
    

# Create your models here.
