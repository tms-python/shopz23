from django.db import models

# Create your models here.
from django.urls import reverse


class Shop(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Наименование магазина'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес магазина'
    )
    staff_amount = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.address}'

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Магазины"
        ordering = (
            'name',
        )


class Department(models.Model):
    SPHERE = (
        ('1', 'Продукты'),
        ('2', 'Игрушки'),
        ('3', 'Одежда')
    )
    sphere = models.CharField(
        max_length=128,
        choices=SPHERE,
        verbose_name='сфера'
    )
    staff_amount = models.IntegerField()
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.DO_NOTHING,
        verbose_name='Магазин'
    )

    def __str__(self):
        return f'{self.get_sphere_display()} {self.shop}'

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = "Департаменты"


class Item(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Наименование товара'
    )
    description = models.CharField(
        max_length=1024,
        verbose_name='Описание товара'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        verbose_name='Департамент'
    )

    def get_absolute_url(self):
        return reverse('shop_app:item_update', args=(self.id,))

    def __str__(self):
        return f'{self.name} {self.price} {self.department}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
        ordering = (
            'name',
            'price',
        )
