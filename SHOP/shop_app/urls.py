from django.urls import path, include
from .views import (
    index,
    ItemListView,
    ItemCreate,
    ItemUpdate,
    ItemDelete,
    IndexView,
)


app_name = 'shop_app'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('item_create/', ItemCreate.as_view(), name='item_create'),
    path('item_update/<int:pk>/', ItemUpdate.as_view(), name='item_update'),
    path('item_delete/<int:pk>/', ItemDelete.as_view(), name='item_delete'),
    path('api/', include('shop_app.api.urls')),
]
