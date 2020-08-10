from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str((self.title, self.content, self.user))

# Create your models here.
