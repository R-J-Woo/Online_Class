from django.urls import path
from rest_framework import routers
from .views import ClassViewSet

router = routers.SimpleRouter()
router.register('classes', ClassViewSet)

urlpatterns = router.urls
