from django.urls import path
from .views import QuestionView

urlpatterns = [
    path('question/<int:pk>/', QuestionView.as_view()),
]
