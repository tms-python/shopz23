from django.core.exceptions import ObjectDoesNotExist
from .models import Department, Shop
from django.db.models import Sum


def change_shop_staff_amount(
        sender: Department,
        instance: Department,
        **kwargs):
    total_shop_staff_amount = \
        sender.objects.filter(shop=instance.shop).\
            aggregate(Sum('staff_amount'))
    print(total_shop_staff_amount, type(total_shop_staff_amount))
    shop = instance.shop
    shop.staff_amount = total_shop_staff_amount['staff_amount__sum']
    shop.save()