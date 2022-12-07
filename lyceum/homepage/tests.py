from catalog.models import Category, Item
from django.test import TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(
            response.status_code,
            200,
        )


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
                name=f'товар {i}',
                text='превосходно',
                is_on_main=bool(i % 2),
                category=cls.Category,
            )

    def test_home_page_show_correct_context(self):
        response = self.client.get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 10)

    def tearDown(self):
        Item.objects.all().delete()
        Category.objects.all().delete()
        super().tearDown()
