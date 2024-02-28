from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    max_page_size = 2
    