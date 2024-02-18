from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comments_by_capsule(request, capsule_id):
    comments = Comment.objects.filter(capsule=capsule_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
