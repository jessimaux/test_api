from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
        title="Snippets API",
        version='v1',
        description="Test description",
        patterns=[path('api/v1/', include('api.urls')), ],
        public=True,
        permission_classes=[permissions.AllowAny,],
    )

urlpatterns = [
    path('openapi', schema_view, name='openapi-schema'),
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]