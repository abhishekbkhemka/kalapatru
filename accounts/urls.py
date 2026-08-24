from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, MeView, UserListCreateView, UserDetailView, RoleListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='auth-login'),
    path('refresh/', TokenRefreshView.as_view(), name='auth-refresh'),
    path('me/', MeView.as_view(), name='auth-me'),
    path('roles/', RoleListView.as_view(), name='auth-roles'),
    path('users/', UserListCreateView.as_view(), name='auth-users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='auth-user-detail'),
]
