from rest_framework import serializers

from ..models import (
    Department,
    Item,
    Shop
)


class DepartmentSerializer(serializers.ModelSerializer):
    sphere_name = serializers.SerializerMethodField()

    def get_sphere_name(self, obj: Department):
        return obj.get_sphere_display()

    class Meta:
        model = Department
        fields = (
            'id',
            'sphere',
            'sphere_name',
            'staff_amount',
            'shop',
        )  # можно указать отдельные поля
        #  ('id', 'some_field')


class ItemSerializer(serializers.ModelSerializer):
    department_obj = DepartmentSerializer(
        source='department',
        read_only=True,
    )

    class Meta:
        model = Item
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
