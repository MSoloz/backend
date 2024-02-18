from django.urls import path
from .views import add_channel, get_all_channels, delete_channel,update_channel


urlpatterns = [
 path('add-channel/', add_channel, name='add-channel'),
 path('all/', get_all_channels, name='get-all-channels'),
 path('update-channel/<int:pk>/', update_channel, name='update-channel'),
 path('delete-channel/<int:pk>/', delete_channel, name='delete-channel'),
]