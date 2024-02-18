from django.urls import path
from .views import add_comment, comments_by_capsule, update_comment, delete_comment

urlpatterns = [
    path('add-comment/', add_comment, name='add-comment'),
    path('<int:capsule_id>/all/', comments_by_capsule, name='comments-by-capsule'),
    path('update-comment/<int:comment_id>/', update_comment, name='update-comment'),
    path('delete-comment/<int:comment_id>/', delete_comment, name='delete-comment'),
]
