from django.urls import path
from . import views


urlpatterns = [

 path('create/',views.create_capsule,name='create_capsule'),
 path('<int:channel_id>/<int:rubric_id>/all/', views.get_capsules_by_channel_and_rubric, name='get_capsules_by_channel_and_rubric'),
 path('<int:capsule_id>/delete/', views.delete_capsule, name='delete_capsule'),
 path('<int:capsule_id>/update/', views.update_capsule, name='update_capsule'),
 path('<int:video_id>/', views.get_video_by_id, name='get_video_by_id'),
 
]