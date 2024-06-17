from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120 )
    status = models.CharField(default='inactive', max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title