from django.urls import path, include
from .views import (
    index,
    ItemListView,
    ItemCreate,
    ItemDetail,
    ItemUpdate,
    ItemDelete,
    IndexView,
    CreateDepartmentAndItem
)


app_name = 'shop_app'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('item_create/', ItemCreate.as_view(), name='item_create'),
    path('item_detail/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('item_update/<int:pk>/', ItemUpdate.as_view(), name='item_update'),
    path('item_delete/<int:pk>/', ItemDelete.as_view(), name='item_delete'),
    path('item_and_department_create/', CreateDepartmentAndItem.as_view(), name='item_and_department_create'),
    path('api/', include('shop_app.api.urls')),
]
