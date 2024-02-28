from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer
from sponsor.serializers import SponsorSerializer
from sponsor.models import Sponsor


@api_view(['GET'])
def events_by_channel(request, channel_id):
    events = Event.objects.filter(channel=channel_id)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer   

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer 

class EventSponsorsView(generics.ListAPIView):
    serializer_class = SponsorSerializer

    def get_queryset(self):
        capsule_id = self.kwargs['pk']
        return Sponsor.objects.filter(id=capsule_id)