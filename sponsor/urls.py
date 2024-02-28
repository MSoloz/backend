from django.urls import path, include
from .views import SponsorListCreateView,SponsorDetailView


urlpatterns = [
     path('/', SponsorListCreateView.as_view(), name='sponsor-list-create'),
     path('/<int:pk>/', SponsorDetailView.as_view(), name='sponsor-detail'),
]
