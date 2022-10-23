from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_int_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/123/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_zero_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_int_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/-123/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_float_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/213.12/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_float_endpoint(self):
        response = Client().get('http://127.0.0.1:8000/catalog/-123.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_endpoint(self):
        response = Client().get('catalog/asdfa2s/')
        self.assertEqual(response.status_code, 404)
