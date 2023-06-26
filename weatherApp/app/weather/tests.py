# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import City

class WeatherAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name='London')

    def test_index_view(self):
        response = self.client.get(reverse('city_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_add_city_view(self):
        response = self.client.post(reverse('add_city'), {'name': 'Paris'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(City.objects.filter(name='Paris').count(), 1)

    def test_delete_city_view(self):
        # Create a test city
        city = City.objects.create(name='Test City')

        # Get the URL for the delete_city view using the reverse function
        url = reverse('delete_city')

        # POST request to delete the city
        response = self.client.post(url, data={'city_name': city.name}, follow=True)

        # Print the response content for debugging
        print(response.content)

        # Assert the status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)

        # Assert the redirect URL is the index view
        self.assertRedirects(response, reverse('city_list'))
