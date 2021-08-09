from django.db import models

from django.contrib.auth.models import User

class QuackerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)


User.quackerprofile = property(lambda u:QuackerProfile.objects.get_or_create(user=u)[0])


