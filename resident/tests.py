
from django.test import TestCase, Client
from django.urls import reverse

from resident.models import User


# Create your tests here.

class HouseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
            phone='1234567890',
            email="aladeamidat@gmail.com"
        )
        self.client = Client()

    def test_that_anonymous_user_cannot_add_house_returns_403(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('add_house')
        data = {
            'house_number': 101,
            'address': '123 Test Street',
            'user': self.user.id
        }
        response = self.client.post(url, data = data)
        self.assertEqual(response.status_code, 403)


    def test_that_resident_user_can_add_house_returns_201(self):
        self.client.login(username='testuser', password='testpassword')

        url = reverse('add_house')
        data = {
            'house_number': 101,
            'address': '123 Test Street',
            'user': self.user.id

        }
        response = self.client.post(url, data = data)
        self.assertEqual(response.status_code, 201)


    def test_that_resident_can_invite_returns_403(self):
        self.client.login(username='testuser', password='testpassword')
        self.assertTrue(self.client.login, "Login failed — check credentials")
        url = reverse('create_invite')
        data = {
                "first_name": "Eniola",
                "last_name": "Jaya",
                "phone_number": "09123456578",
                "expires_at": "2025-08-30"

        }
        response = self.client.post(url, data = data)
        self.assertEqual(response.status_code, 401)


