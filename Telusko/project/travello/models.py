from django.db import models

# Create your models here.
class Course(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    time = models.TimeField()
    fee = models.IntegerField()
    img = models.ImageField(upload_to='pics')

