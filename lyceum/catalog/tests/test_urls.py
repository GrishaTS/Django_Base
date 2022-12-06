from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_item_detail_endpoint(self):
        endpoint_status = {
            200: (
                '/catalog/',
            ),
            404: (
                '/catalog/10/',
                '/catalog/6/',
                '/catalog/-645/',
                '/catalog/0/',
                '/catalog/-0/',
                '/catalog/fdafdj/',
                '/catalog/234str/',
                '/catalog/str248359/',
                '/catalog/str248359asdf/',
                '/catalog/248359asdf231/',
                '/catalog/0234/',
                '/catalog/-0234/',
                '/catalog/00000/',
                '/catalog/-00000/',
                '/catalog/@123/',
                '/catalog/123(/',
                '/catalog/213+2345/',
                '/catalog/-645dasd/',
                '/catalog/0asd/',
                '/catalog/asdf0/',
                '/catalog/fdafdj_/',
                '/catalog/2.34:/',
                '/catalog/12+42-345*213/',
                r'/catalog/(?P<pk>[1-9]\d*)/$/',
            ),
        }
        for status, endpoint_list in endpoint_status.items():
            for endpoint in endpoint_list:
                with self.subTest(endpoint=endpoint):
                    response = Client().get(endpoint)
                    self.assertEqual(
                        response.status_code,
                        status,
                    )
