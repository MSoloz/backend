from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourwebsite.com/terms/",
        contact=openapi.Contact(email="contact@yourwebsite.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('user.urls')),
    path('api/channels/',include('channel.urls')),
    path('api/videos/', include('capsule.urls')),
    path('api/rubrics/', include('rubric.urls')),
    path('api/conditions/', include('condition.urls')),
    path('api/banners/', include('banner.urls')),
    path('api/events/', include('event.urls')),
    path('api/likes/', include('like.urls')),
    path('api/comments/', include('comment.urls')),
    path('api/notes/', include('note.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
