from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_p_int_endpoint(self):
        response = Client().get('/catalog/4783/')
        self.assertEqual(response.status_code, 200)

    def test_one_endpoint(self):
        response = Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_n_int_endpoint(self):
        response = Client().get('/catalog/-645/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_zero_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_zero_endpoint(self):
        response = Client().get('/catalog/-0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_endpoint(self):
        response = Client().get('/catalog/fdafdj/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_int_str_endpoint(self):
        response = Client().get('/catalog/234str/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_int_endpoint(self):
        response = Client().get('/catalog/str248359/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_int_str_endpoint(self):
        response = Client().get('/catalog/str248359asdf/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_int_str_int_endpoint(self):
        response = Client().get('/catalog/248359asdf231/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_zero_int_endpoint(self):
        response = Client().get('/catalog/0234/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_zero_int_endpoint(self):
        response = Client().get('/catalog/-0234/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_5_zero_endpoint(self):
        response = Client().get('/catalog/00000/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_5_zero_endpoint(self):
        response = Client().get('/catalog/-00000/')
        self.assertEqual(response.status_code, 404)

    def test_special_symbol_int_endpoint(self):
        response = Client().get('/catalog/@123/')
        self.assertEqual(response.status_code, 404)

    def test_int_special_symbol_endpoint(self):
        response = Client().get('/catalog/123(/')
        self.assertEqual(response.status_code, 404)

    def test_int_special_symbol_int_endpoint(self):
        response = Client().get('/catalog/213+2345/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_n_int_str_endpoint(self):
        response = Client().get('/catalog/-645dasd/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_zero_str_endpoint(self):
        response = Client().get('/catalog/0asd/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_zero_endpoint(self):
        response = Client().get('/catalog/asdf0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_special_symbol_endpoint(self):
        response = Client().get('/catalog/fdafdj_/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_float_special_symbol_endpoint(self):
        response = Client().get('/catalog/2.34:/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_math_operation_endpoint(self):
        response = Client().get('/catalog/12+42-345*213/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_str_endpoint(self):
        response = Client().get(r'/catalog/(?P<pk>^[1-9]\d*)/$/')
        self.assertEqual(response.status_code, 404)
