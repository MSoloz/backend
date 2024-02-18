from django.urls import path
from . import views

urlpatterns = [
 path('create/',views.create_rubric),
 path('<int:channel_id>/all/',views.get_all_rubrics_by_channel_id),
 path('<int:pk>/update/',views.update_rubric),
 path('<int:pk>/delete/',views.delete_rubric),
]