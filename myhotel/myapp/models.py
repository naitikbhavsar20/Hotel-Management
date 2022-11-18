from django.db import models

# Create your models here.

class myapp(models.Model):
    fname = models.CharField(max_length=30, primary_key=True)
    lname= models.CharField(max_length=30)
    email= models.CharField(max_length=100)
    mobile= models.CharField(max_length=100)
    num= models.CharField(max_length=100)
    rtype= models.CharField(max_length=100)
    date= models.CharField(max_length=100)