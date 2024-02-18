from django.urls import path
from .views import add_notification, delete_notification, update_notification, get_all_notifications_by_user_id

urlpatterns = [
    path('add-notification/', add_notification, name='add_notification'),
    path('delete/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('update/<int:notification_id>/', update_notification, name='update_notification'),
    path('all/<int:user_id>/', get_all_notifications_by_user_id, name='get_all_notifications_by_user'),
]
