from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer

@api_view(['POST'])
def add_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def events_by_channel(request, channel_id):
    events = Event.objects.filter(channel=channel_id)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

