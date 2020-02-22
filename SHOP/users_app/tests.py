from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.

USERNAME = 'admin'
PASSWORD = 'zaq1@WSX'


class TestAuth(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username=USERNAME,
            is_superuser=True,
            password=PASSWORD
        )
        self.text_on_login_page = 'Имя пользователя'

    def testRequestRootUrl(self):
        response = self.client.get('/', follow=True)
        print(response.redirect_chain)
        print(response.redirect_chain[0])
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.text_on_login_page)

    def testAuthUrl(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.text_on_login_page)

    def testAuth(self):
        response = self.client.post(
            '/user/login/',
            {'username': USERNAME, 'password': PASSWORD}
        )
        self.assertEqual(response.status_code, 200)

    def testLogout(self):
        self.client.post(
            '/user/login/',
            {'username': USERNAME, 'password': PASSWORD}
        )
        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, 200)

    def testLogoutFollowRedirect(self):
        self.client.post('/user/login/', {'username': USERNAME, 'password': PASSWORD})
        response = self.client.get('/user/logout/', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
