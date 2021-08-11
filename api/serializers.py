from django.contrib.auth.models import User

from rest_framework import serializers

from quacks.models import Quack

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quack
        fields = ['body', 'author', 'date_created']