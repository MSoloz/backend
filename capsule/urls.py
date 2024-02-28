from django.urls import path
from . import views
from .views import CapsuleDetailView,CapsuleListCreateView,CapsuleSponsorsView


urlpatterns = [

 path('<int:channel_id>/<int:rubric_id>/all/', views.get_capsules_by_channel_and_rubric, name='get_capsules_by_channel_and_rubric'),
 path('<int:pk>/', CapsuleDetailView.as_view(),name='capsule_list_create'),
 path('', CapsuleListCreateView.as_view(),name='capsule_detail'),
 path('<int:pk>/sponsors/', CapsuleSponsorsView.as_view(), name='capsule-sponsors'),
 
]