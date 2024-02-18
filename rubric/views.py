from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rubric
from .serializers import RubricSerializer


@api_view(['POST'])
def create_rubric(request):
    serializer = RubricSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_rubrics_by_channel_id(request, channel_id):
    rubrics = Rubric.objects.filter(channel_id=channel_id)
    serializer = RubricSerializer(rubrics, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_rubric(request, pk):
    try:
        rubric = Rubric.objects.get(pk=pk)
    except Rubric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    rubric.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_rubric(request, pk):
    try:
        rubric = Rubric.objects.get(pk=pk)
    except Rubric.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = RubricSerializer(rubric, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


