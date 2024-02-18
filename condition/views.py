from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Condition
from .serializers import ConditionSerializer

@api_view(['POST'])
def create_condition(request):
    serializer = ConditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_condition_by_channel_id(request, channel_id):
    conditions = Condition.objects.filter(channel_id=channel_id)
    serializer = ConditionSerializer(conditions, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_condition(request, condition_id):
    try:
        condition = Condition.objects.get(pk=condition_id)
    except Condition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ConditionSerializer(condition, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_condition(request, condition_id):
    try:
        condition = Condition.objects.get(pk=condition_id)
    except Condition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    condition.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
