from django.contrib import admin
from django.urls import path, include
from djoser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/main/', include('main_app.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path("auth/token/login", views.UserViewSet.create.as_view(), name="login"),
    # path("auth/token/logout", views.TokenDestroyView.as_view(), name="logout"),
    # path("auth/users", views.UserCreateView.as_view(), name="create user"),
    # path("auth/users/activation", views.ActivationView.as_view(), name="activate user"),
    # path("auth/users/me", views.UserView.as_view(), name="info user"),
]
