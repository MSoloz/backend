from django.urls import path
from .views import add_note, notes_by_user, update_note, delete_note

urlpatterns = [
    path('add-note/', add_note, name='add-note'),
    path('<int:user_id>/', notes_by_user, name='notes-by-user'),
    path('update-note/<int:note_id>/', update_note, name='update-note'),
    path('delete-note/<int:note_id>/', delete_note, name='delete-note'),
]
