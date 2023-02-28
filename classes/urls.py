from django.urls import path
from rest_framework import routers
from .views import ClassViewSet, RecommendView, JoinView

router = routers.SimpleRouter()
router.register('classes', ClassViewSet)

urlpatterns = router.urls + [
    path('recommend/<int:pk>/', RecommendView.as_view()),
    path('join/<int:pk>/', JoinView.as_view())
]
