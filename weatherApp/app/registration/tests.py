from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import City

class ViewsTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.city_name = 'New York'
        self.city = City.objects.create(name=self.city_name, user=self.user)

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful registration
        self.assertEqual(User.objects.count(), 2)  # User count should be incremented

    def test_user_login_view(self):
        response = self.client.post(reverse('user_login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login

    def test_user_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect after successful logout

    def test_index_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('city_list'))
        self.assertEqual(response.status_code, 200)  # Should return 200 for successful login
        self.assertContains(response, self.city_name)  # Should contain the city in the weather list

    def test_add_city_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('add_city'), {
            'name': 'Chicago',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after adding a city
        self.assertEqual(City.objects.count(), 2)  # City count should be incremented

    def test_delete_city_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('delete_city'), {
            'name': self.city_name,
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after deleting a city
        self.assertEqual(City.objects.count(), 0)  # City count should be decremented
