from django.urls import path, include
from .views import UserApi, UserDetailApi

urlpatterns = [
    path('users/', UserApi.as_view()),
    path('userdetail/<int:pk>', UserDetailApi.as_view())
]