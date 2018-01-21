from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_path = models.CharField(max_length=200)
    description =  models.TextField()
    created_at = models.DateTimeField(default=timezone.now)