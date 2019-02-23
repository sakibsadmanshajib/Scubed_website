from django.db import models
from django.utils import timezone

# Create your models here.

class Subscriber(models.Model):
    Timestamp = models.DateTimeField(default=timezone.now())
    Name = models.CharField(max_length=128)
    Email = models.EmailField()

    def __str__(self):
        return self.Name