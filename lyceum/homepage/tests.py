from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
