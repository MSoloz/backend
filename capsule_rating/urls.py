from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_rating, name='create_rating'),
    path('<int:capsule_id>/capsule/', views.get_rating_by_capsule_id, name='get_rating_by_capsule_id'),
    path('<int:rating_id>/update/', views.update_rating, name='update_rating'),
    path('<int:rating_id>/delete/', views.delete_rating, name='delete_rating'),
]
