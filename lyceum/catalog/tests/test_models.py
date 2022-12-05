from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Category, Item, Tag


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
                    text=i,
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
        ], start=1):
            self.item = Item(
                name='Товар-велосипед' + str(i[0]),
                category=self.Category,
                text=i[1],
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.Tag)
            self.assertEqual(
                Item.objects.count(),
                item_count + i[0],
            )
