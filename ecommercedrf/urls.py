"""
ecommercedrf URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from ecommercedrf.product.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category", CategoryViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]
