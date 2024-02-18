from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rating
from .serializers import RatingSerializer

@api_view(['POST'])
def create_rating(request):
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_rating_by_capsule_id(request, capsule_id):
    ratings = Rating.objects.filter(capsule_id=capsule_id)
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_rating(request, rating_id):
    try:
        rating = Rating.objects.get(id=rating_id)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RatingSerializer(rating, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_rating(request, rating_id):
    try:
        rating = Rating.objects.get(id=rating_id)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

