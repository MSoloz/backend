from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_banner, name='add_banner'),
    path('<int:channel_id>/<int:rubric_id>/', views.get_banner_by_channel_and_rubric, name='get_banner'),
    path('update_banner/<int:banner_id>/', views.update_banner, name='update_banner'),
    path('delete_banner/<int:banner_id>/', views.delete_banner, name='delete_banner'),
]
