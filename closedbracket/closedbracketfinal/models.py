from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    
