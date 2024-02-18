from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from capsule.models import Capsule
from capsule.serializers import CapsuleSerializer
from user.models import CustomUser
from .models import Like
from .serializers import LikeSerializer

@api_view(['POST'])
def add_like(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def likes_by_user(request, user_id):
    likes = Like.objects.filter(user=user_id)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_like(request, like_id):
    like = Like.objects.get(pk=like_id)
    serializer = LikeSerializer(like, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_like(request, like_id):
    like = Like.objects.get(pk=like_id)
    like.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def liked_capsules_by_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    likes = Like.objects.filter(user=user)
    liked_capsule_ids = [like.capsule.id for like in likes]
    liked_capsules = Capsule.objects.filter(id__in=liked_capsule_ids)
    serializer = CapsuleSerializer(liked_capsules, many=True)
    return Response(serializer.data)