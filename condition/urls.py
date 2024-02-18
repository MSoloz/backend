from django.urls import path
from . import views 

urlpatterns = [
    path('create/', views.create_condition, name='create_condition'),
    path('get/<int:channel_id>/', views.get_condition_by_channel_id, name='get_condition_by_channel_id'),
    path('update/<int:condition_id>/', views.update_condition, name='update_condition'),
    path('delete/<int:condition_id>/', views.delete_condition, name='delete_condition'),
]
