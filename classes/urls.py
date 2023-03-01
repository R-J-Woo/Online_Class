from django.urls import path
from rest_framework import routers
from .views import ClassViewSet, RecommendView, JoinView

router = routers.SimpleRouter()
router.register('classes', ClassViewSet)

urlpatterns = router.urls + [
    path('classes/<int:pk>/recommend/', RecommendView.as_view()),
    path('classes/<int:pk>/join/', JoinView.as_view())
]
