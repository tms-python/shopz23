from django.db import models
from PIL import Image

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
    is_delete = models.BooleanField(
        default=False,
        verbose_name='Удалено'
    )

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    def save(self, *agrs, **kwargs):
        return super(Department, self).save(*agrs, **kwargs)

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
    image = models.ImageField(
        upload_to='image/shop_app/%Y/%m/%d',
        default=None,
        blank=True,
        null=True,
        verbose_name='Изображения'
    )

    def save(self, *args, **kwargs):
        try:
            this_entry = Item.objects.get(id=self.id)
            if this_entry.image != self.image:
                this_entry.image.delete(save=False)
        except:
            pass
        super(Item, self).save(*args, **kwargs)
        image = Image.open(self.image.path)
        max_size = max(image.size[0], image.size[1])
        multiplier = max_size / 1200
        image = image.resize((round(image.size[0] / multiplier), round(image.size[1] / multiplier)), Image.ANTIALIAS)
        image.save(self.image.path)
        print(image.size)

        image.save(self.image.path)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)

        super(Item, self).delete(*args, **kwargs)

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
