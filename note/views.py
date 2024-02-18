from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['POST'])
def add_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def notes_by_user(request, user_id):
    notes = Note.objects.filter(user=user_id)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

