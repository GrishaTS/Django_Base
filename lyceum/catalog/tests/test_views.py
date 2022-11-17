from django.test import Client, TestCase
from django.urls import reverse

from ..models import Category, Item


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Category = Category.objects.create(
            name='Велосипед',
            slug='Bicycle',
        )
        for i in range(20):
            cls.Item = Item.objects.create(
                name=f'товар{i}',
                text='превосходно',
                is_published=bool(i % 2),
                category=cls.Category,
            )

    def test_item_list_page_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context), 14)
