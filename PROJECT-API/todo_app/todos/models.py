from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    author = models.ForeignKey(User,null=True, default=None,on_delete=models.CASCADE)
    todo = models.CharField(max_length = 200)
    is_completed = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author