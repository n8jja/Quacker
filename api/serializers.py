from django.contrib.auth.models import User

from rest_framework import serializers

from quacks.models import Quack

class FeedSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedFields(read_only=True)

    class Meta:
        model = Quack
        fields = '__all__'

