from django.urls import path
from .views import UserListCreateView, UserDetailView,UserDeleteByIDView, UserUpdateByIDView

urlpatterns = [
    # User-related endpoints
    path('users/', UserListCreateView.as_view(), name='user-list-create'),  # List and Sign Up
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve,
    path('users/delete/<int:user_id>/', UserDeleteByIDView.as_view(), name='user-delete-by-id'),
    path('users/update/<int:user_id>/', UserUpdateByIDView.as_view(), name='user-update-by-id'),
]
