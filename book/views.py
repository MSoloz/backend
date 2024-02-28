from rest_framework import generics
from .models import Book
from .pagination import BookPagination


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    
    pagination_class = BookPagination
    



class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()



