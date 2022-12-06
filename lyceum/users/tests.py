from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from users.models import Profile


class UsersProcessorTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Profile = Profile.objects.create(
            email='user@user.ru',
            password='smartuser',
            birthday=datetime.today(),
        )

    def test_show_users_context(self):
        urls = [
            'about:description',
            'catalog:item_list',
            'feedback:feedback',
            'homepage:home',
            'users:user_list',
            'users:signup',
        ]
        for value in urls:
            with self.subTest("Failed to open url", value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 1)
                user = response.context['users'][0]
                self.assertIn('email', user)
                self.assertEqual(user['email'], 'user@user.ru')

    def test_show_empty_context(self):
        self.Profile.delete()
        urls = [
            'about:description',
            'catalog:item_list',
            'feedback:feedback',
            'homepage:home',
            'users:user_list',
            'users:signup',
        ]
        for value in urls:
            with self.subTest("Failed to open url", value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 0)

    def test_show_several_users_context(self):
        Profile.objects.create(
            email='user2@user.ru',
            password='smartuser2',
            birthday=datetime.today(),
        )

        urls = [
            'about:description',
            'catalog:item_list',
            'feedback:feedback',
            'homepage:home',
            'users:user_list',
            'users:signup',
        ]
        for value in urls:
            with self.subTest("Failed to open url", value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 2)

    def test_show_user_another_birthday_context(self):
        tomorrow = datetime.today() + timedelta(days=1)
        Profile.objects.create(
            email='user2@user.ru',
            password='smartuser2',
            birthday=tomorrow,
        )

        urls = [
            'about:description',
            'catalog:item_list',
            'feedback:feedback',
            'homepage:home',
            'users:user_list',
            'users:signup',
        ]
        for value in urls:
            with self.subTest("Failed to open url", value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 1)
                user = response.context['users'][0]
                self.assertIn('email', user)
                self.assertEqual(user['email'], 'user@user.ru')

    def tearDown(self):
        Profile.objects.all().delete()
        super().tearDown()
