from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new

schema_view = get_schema_view(openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ))

urlpatterns = [
    path('openapi', schema_view.as_view(), name='openapi-schema'),
    path('swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]