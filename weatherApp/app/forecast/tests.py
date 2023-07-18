from django.test import TestCase
from django.urls import reverse

class DetailsViewTestCase(TestCase):
    def setUp(self):
        self.city_name = 'New York'
        self.api_key = 'your_api_key_here'  # Replace with your valid API key

    def test_details_view(self):
        response = self.client.get(reverse('details', args=[self.city_name]))
        self.assertEqual(response.status_code, 200)  # Should return 200 for successful request
        self.assertContains(response, self.city_name)  # Should contain the city name in the response content
        self.assertContains(response, 'datetime')  # Should contain the forecast datetime
        self.assertContains(response, 'temperature')  # Should contain the forecast temperature
        self.assertContains(response, 'weather')  # Should contain the forecast weather
        self.assertContains(response, 'description')  # Should contain the forecast description
