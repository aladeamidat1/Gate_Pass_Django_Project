
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




