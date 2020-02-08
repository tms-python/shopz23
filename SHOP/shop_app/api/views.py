from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    DepartmentSerializer,
    ItemSerializer,
    ShopSerializer
)

from ..models import (
    Department,
    Item,
    Shop
)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.filter(is_delete=False)
    # queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        print('HI i am list method')
        return super(DepartmentViewSet, self).list(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def all_instances(self, request, *args, **kwargs):
        queryset = Department.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



    # def retrieve(self, request, *args, **kwargs):  #  получение отдельной объект
    # def create(self, request, *args, **kwargs):    #  создание сущности объекта
    # def update(self, request, *args, **kwargs):    #  обновление объекта
    # def destroy(self, request, *args, **kwargs):   #  удаление объекта


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    # queryset = Department.objects.all()
    serializer_class = ItemSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    # queryset = Department.objects.all()
    serializer_class = ShopSerializer