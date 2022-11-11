from http import HTTPStatus

from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from .models import Category, Item, OneImage, Tag


class StaticURLTests(TestCase):
    def test_item_detail_endpoint(self):
        endpoint_status = {
            HTTPStatus.OK: (
                '/catalog/',
                '/catalog/4783/',
                '/catalog/1/',
            ),
            HTTPStatus.NOT_FOUND: (
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
                r'/catalog/(?P<pk>^[1-9]\d*)/$/',
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
        cls.OneImage = OneImage.objects.create(name='изображение')

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
                    text=i,
                    preview=self.OneImage,
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
        for i in enumerate(['превосходно',
                            'роскошно слово',
                            'не,роскошно!',
                            'Превосходно платье',
                            ',превосходно.',
                            ],
                           start=1,
                           ):
            self.item = Item(
                name='Товар-велосипед',
                category=self.Category,
                text=i[1],
                preview=OneImage.objects.create(
                    name='изображение' + str(i[0])
                ),
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.Tag)
            self.assertEqual(
                Item.objects.count(),
                item_count + i[0],
            )
