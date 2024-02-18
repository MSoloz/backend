from django.urls import path
from .views import add_event, events_by_channel, update_event, delete_event

urlpatterns = [
    path('add-event/', add_event, name='add-event'),
    path('all/<int:channel_id>/', events_by_channel, name='events-by-channel'),
    path('update-event/<int:event_id>/', update_event, name='update-event'),
    path('delete-event/<int:event_id>/', delete_event, name='delete-event'),
]
