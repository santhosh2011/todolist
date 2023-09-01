from django.db import models
from django.utils import timezone


class Todo(models.Model):
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
