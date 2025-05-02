from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True)
    task = models.CharField(max_length=255)
    completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)