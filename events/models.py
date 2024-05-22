from django.db import models

# Create your models here.

class Comment(models.Model):
    username = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)