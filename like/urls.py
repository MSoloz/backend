from django.urls import path
from .views import add_like, likes_by_user, update_like, delete_like, liked_capsules_by_user

urlpatterns = [
    path('add-like/', add_like, name='add-like'),
    path('<int:user_id>/', likes_by_user, name='likes-by-user'),
    path('update-like/<int:like_id>/', update_like, name='update-like'),
    path('delete-like/<int:like_id>/', delete_like, name='delete-like'),
    path('liked-capsules/<int:user_id>/', liked_capsules_by_user, name='liked_capsules_by_user'),
]
