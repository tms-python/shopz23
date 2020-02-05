from rest_framework import routers
from django.conf.urls import include
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('department', views.DepartmentViewSet)
router.register('item', views.ItemViewSet)
router.register('shop', views.ShopViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

