from rest_framework import routers
from django.conf.urls import include
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('department', views.DepartmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

