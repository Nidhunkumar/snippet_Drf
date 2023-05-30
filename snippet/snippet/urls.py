"""snippet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from app.views import (
    UserRegistration,
    SnippetView,
    SnippetDetailView,
    TagListView,
    SnippetByTagView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)





urlpatterns = [
    path('admin/', admin.site.urls),


        path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),

    path('api/register/', UserRegistration.as_view()),

    path('api/snippet/', SnippetView.as_view(), name='snippet'),
    path('api/snippet/add/', SnippetView.as_view(), name='snippet-add'),
    path('api/snippet/<id>/', SnippetDetailView.as_view(), name='snippet-details'),
    path('api/snippet/delete/<id>/', SnippetDetailView.as_view(), name='snippet-delete'),
    path('api/snippet/edit/<id>/', SnippetDetailView.as_view(), name='snippet-edit'),

    path('api/tag/list/', TagListView.as_view(), name='tags'),
    path('api/snippet/list/<tag_id>/', SnippetByTagView.as_view(), name='snippet-by-tag-id'),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),





]
