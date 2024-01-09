from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    def __str__(self):
        return self.title

