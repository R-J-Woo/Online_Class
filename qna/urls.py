from django.urls import path
from .views import QuestionViewSet, AnswerViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)

urlpatterns = router.urls
