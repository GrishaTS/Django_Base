from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Item, Tag


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


class TestsForModels(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Category = Category.objects.create(
            name='Велосипед',
            slug='Bicycle',
        )
        cls.Tag = Tag.objects.create(
            name='До 20000 руб',
            slug='less-than-20000',
        )

    def test_invalid(self):
        item_count = Item.objects.count()
        for i in ['нет нужных слов',
                  'Слово нероскошное',
                  'превосходное чувство',
                  'нероскошное слово',
                  'Превосходное платье',
                  'нероск.ош!но',
                  ]:
            with self.assertRaises(ValidationError):
                self.item = Item(
                    name='Товар-велосипед',
                    category=self.Category,
                    text=i
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.Tag)
            self.assertEqual(
                Item.objects.count(),
                item_count,
            )

    def test_valid(self):
        item_count = Item.objects.count()
        for i in enumerate([
            'превосходно',
            'роскошно слово',
            'не,роскошно!',
            'Превосходно платье',
            ',превосходно.',
        ], start=1, ):
            self.item = Item(
                name='Товар-велосипед' + str(i[0]),
                category=self.Category,
                text=i[1]
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.Tag)
            self.assertEqual(
                Item.objects.count(),
                item_count + i[0],
            )


class TaskPagesTests(TestCase):
    def test_home_page_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context), 4)
