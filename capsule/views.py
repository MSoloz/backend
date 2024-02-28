from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Capsule
from .serializers import CapsuleSerializer
from sponsor.serializers import SponsorSerializer
from sponsor.models import Sponsor
from .pagination import CustomPageNumberPagination

    
@api_view(['GET'])
def get_capsules_by_channel_and_rubric(request, channel_id, rubric_id):
    try:
        capsules = Capsule.objects.filter(channel_id=channel_id, rubric_id=rubric_id)
        serializer = CapsuleSerializer(capsules, many=True)
        return Response(serializer.data)
    except Capsule.DoesNotExist:
        return Response(status=404)
    
   
class CapsuleListCreateView(generics.ListCreateAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer

class CapsuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer  

class CapsuleSponsorsView(generics.ListAPIView):
    serializer_class = SponsorSerializer

    def get_queryset(self):
        capsule_id = self.kwargs['pk']
        return Sponsor.objects.filter(id=capsule_id)

