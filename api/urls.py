from django.urls import path
from .views.user import HomeView, UserView, UserLoginView

urlpatterns = [
    path('', HomeView.as_view(), name="home")
]