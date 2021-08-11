from rest_framework import routers
from .views import FeedViewset

router = routers.DefaultRouter()
router.register('quacks', FeedViewset)

urlpatterns = router.urls