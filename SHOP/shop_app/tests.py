from django.contrib.auth.models import User
from django.test import TestCase
from .models import Shop, Department, Item

# Create your tests here.

USERNAME = 'admin'
PASSWORD = 'zaq1@WSX'

class TestShop(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(
            name='MyShop',
            address='SomeStr',
        )

        self.department = Department()
        self.department.staff_amount = 100
        self.department.shop = self.shop
        self.department.sphere = '1'
        self.department.is_delete = False
        self.department.save()

        self.item = Item()
        self.item.department = self.department
        self.item.description = 'description Some self.item'
        self.item.name = 'Item name'
        self.item.price = 123
        self.item.save()

        self.user = User.objects.create(
            username=USERNAME,
            is_superuser=True,
            password=PASSWORD
        )

    def testCreateItem(self):
        self.client.post(
            '/user/login/',
            {'username': USERNAME, 'password': PASSWORD}
        )

        response = self.client.post('/item_create/', {
            'name': 'new_item',
            'description': 'some_description',
            'department': self.department.id,
            'price': 500
        }, follow=True)

        self.assertContains(
            response,
            text='Обновить',
            status_code=200
        )

        new_item = Item.objects.get(name='new_item', price=500)

        self.assertEqual(new_item.name, 'new_item')
        self.assertEqual(new_item.description, 'some_description')