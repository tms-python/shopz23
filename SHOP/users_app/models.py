from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Профиль пользователя'
    )
    address = models.CharField(
        max_length=512,
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name='Телефон',
        blank=True,
        null=True,
    )

    def __str__(self):
        print(self.__getattribute__('phone_number'))
        return f'{self.user.username} {self.user.email}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = (
            'phone_number',
        )
