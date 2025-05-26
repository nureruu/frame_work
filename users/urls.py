# users/urls.py
from django.urls import path
from .views import RegisterView, ConfirmUserView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('confirm/', ConfirmUserView.as_view()),
    path('login/', LoginView.as_view()),
]
