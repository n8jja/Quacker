from quacks.models import Quack
from rest_framework import viewsets, permissions
from .serializers import FeedSerializer

class FeedViewset(viewsets.ModelViewSet):
    queryset = Quack.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]

