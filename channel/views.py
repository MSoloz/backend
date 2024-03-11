from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Channel
from .serializers import ChannelSerializer


@api_view(['POST'])
def add_channel(request):
    serializer = ChannelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_channels(request):
    channels = Channel.objects.all()
    serializer = ChannelSerializer(channels, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_channel(request, pk):
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    channel.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_channel(request, pk):
    try:
        channel = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChannelSerializer(channel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_channels_by_user(request, user_id):
    channels = Channel.objects.filter(user_id=user_id)
    serializer = ChannelSerializer(channels, many=True)
    return Response(serializer.data)