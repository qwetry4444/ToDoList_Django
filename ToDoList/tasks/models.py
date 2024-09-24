from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tasks(models.Model):
    text = models.TextField(blank=True, default="")
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tasks"
