from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title