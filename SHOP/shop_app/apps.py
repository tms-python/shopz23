from django.apps import AppConfig
from django.db.models.signals import post_save


class ShopAppConfig(AppConfig):
    name = 'shop_app'

    def ready(self):
        from .signals import change_shop_staff_amount
        Department = self.get_model('Department')
        post_save.connect(change_shop_staff_amount, sender=Department)