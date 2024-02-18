from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Capsule
from .serializers import CapsuleSerializer


@api_view(['POST'])
def create_capsule(request):
    serializer = CapsuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_capsules_by_channel_and_rubric(request, channel_id, rubric_id):
    try:
        capsules = Capsule.objects.filter(channel_id=channel_id, rubric_id=rubric_id)
        serializer = CapsuleSerializer(capsules, many=True)
        return Response(serializer.data)
    except Capsule.DoesNotExist:
        return Response(status=404)
    
@api_view(['DELETE'])
def delete_capsule(request, capsule_id):
    try:
        capsule = Capsule.objects.get(id=capsule_id)
        capsule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Capsule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_capsule(request, capsule_id):
    try:
        capsule = Capsule.objects.get(id=capsule_id)
    except Capsule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CapsuleSerializer(capsule, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_video_by_id(request, video_id):
    try:
        video = Capsule.objects.get(id=video_id)
        serializer = CapsuleSerializer(video)
        return Response(serializer.data)
    except Capsule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)