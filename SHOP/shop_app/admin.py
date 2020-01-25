from django.contrib import admin

from .models import (
    Shop,
    Department,
    Item
)
# Register your models here.

admin.site.register(Shop)
admin.site.register(Department)
admin.site.register(Item)
