from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Banner
from .serializers import BannerSerializer


@api_view(['POST'])
def add_banner(request):
    serializer = BannerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_banner_by_channel_and_rubric(request, channel_id, rubric_id):
    try:
        banner = Banner.objects.get(channel_id=channel_id, rubric_id=rubric_id)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BannerSerializer(banner)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_banner(request, banner_id):
    try:
        banner = Banner.objects.get(pk=banner_id)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BannerSerializer(banner, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_banner(request, banner_id):
    try:
        banner = Banner.objects.get(pk=banner_id)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    banner.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

