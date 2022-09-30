from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'women', views.WomenViewSet)

urlpatterns = [
    path('api/v1/women/', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('api/v1/category/', views.CategoryAPIList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist', views.WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', views.WomenViewSet.as_view({'put': 'update'})),
]