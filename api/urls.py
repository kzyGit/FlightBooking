from django.urls import path
from .views.user import HomeView, UserView, UserLoginView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('users/', UserView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login')
]