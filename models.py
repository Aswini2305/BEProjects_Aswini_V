from django.db import models


# Create your models here.
class Questions(models.Model):
    question =models.TextField()
    
    options1=models.CharField(max_length=100)
    options2=models.CharField(max_length=100) 
    options3=models.CharField(max_length=100) 
    options4=models.CharField(max_length=100)

     
    answer=models.CharField(max_length=100)