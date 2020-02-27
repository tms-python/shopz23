from django import forms
from .models import (
    Item,
    Department,
)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ItemWithoutDepartmentForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = (
            'department',
            'is_deleted',
        )


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = (
            'is_delete',
        )