from django.db import models
from django.contrib.auth.models import User


class Quack(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(User, related_name='quacks', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
