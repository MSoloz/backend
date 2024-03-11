from django.urls import path
from .views import add_channel, get_all_channels, delete_channel,update_channel,get_channels_by_user


urlpatterns = [
 path('add-channel/', add_channel, name='add-channel'),
 path('all/', get_all_channels, name='get-all-channels'),
 path('update-channel/<int:pk>/', update_channel, name='update-channel'),
 path('delete-channel/<int:pk>/', delete_channel, name='delete-channel'),
  path('<int:user_id>/all/', get_channels_by_user, name='get-channels-by-user'),
]