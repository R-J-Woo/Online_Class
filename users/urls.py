from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('sign-up/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
]
