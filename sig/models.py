from django.db import models
from uuid import uuid4
# Create your models here.
class Topics(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=10)
    description = models.TextField(null=False, blank=False)
    def __str__(self):
        return f"{self.name}"