from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from channel.models import Channel
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['POST'])
def add_notification(request):
    if request.method == 'POST':
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    notification.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NotificationSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_notifications_by_user_id(request, user_id):
    notifications = Notification.objects.filter(user__id=user_id)
    serializer = NotificationSerializer(notifications, many=True)

    data_with_channel_info = []
    for notification_data in serializer.data:
        channel_id = notification_data.pop('channel')  # Removing 'channel' from the original data
        try:
            channel = Channel.objects.get(id=channel_id)
            notification_data['channel_title'] = channel.title
            notification_data['channel_icon'] = channel.icon_path.url
        except Channel.DoesNotExist:
            notification_data['channel_title'] = None
            notification_data['channel_icon'] = None
        data_with_channel_info.append(notification_data)

    return Response(data_with_channel_info)
