from django.urls import path
from .views import events_by_channel
from .views import EventListCreateView,EventDetailView,EventSponsorsView

urlpatterns = [
    path('all/<int:channel_id>/', events_by_channel, name='events-by-channel'),
    path('<int:pk>/', EventDetailView.as_view(),name='event_list_create'),
    path('', EventListCreateView.as_view(),name='event_detail'),
    path('<int:pk>/sponsors/', EventSponsorsView.as_view(), name='event-sponsors'),
]
