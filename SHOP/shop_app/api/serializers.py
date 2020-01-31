from rest_framework import serializers

from ..models import (
    Department,
)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'sphere',
            'staff_amount',
            'shop',
        )  # можно указать отдельные поля
        #  ('id', 'some_field')
