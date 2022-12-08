from datetime import date, timedelta
from unittest import mock

from django.test import TestCase
from django.urls import reverse

from core import date_util
from users.models import Profile


class UsersProcessorTests(TestCase):
    @classmethod
    @mock.patch('core.date_util.today')
    def setUpClass(cls, mock_today):
        super().setUpClass()
        cls.fake_today = date(2020, 1, 1)
        mock_today.return_value = cls.fake_today
        cls.profile = Profile.objects.create(
            email='user@user.ru',
            password='smartuser',
            birthday=date_util.today(),
        )
        cls.urls = [
            'about:description',
            'catalog:item_list',
            'feedback:feedback',
            'homepage:home',
            'users:user_list',
            'users:signup',
        ]

    @mock.patch('core.date_util.today')
    def test_show_users_context(self, mock_today):
        mock_today.return_value = self.fake_today
        for value in self.urls:
            with self.subTest('Failed to open url', value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 1)
                user = response.context['users'][0]
                self.assertIn('email', user)
                self.assertEqual(user['email'], 'user@user.ru')

    def test_show_empty_context(self):
        self.profile.delete()
        for value in self.urls:
            with self.subTest('Failed to open url', value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 0)

    @mock.patch('core.date_util.today')
    def test_show_several_users_context(self, mock_today):
        mock_today.return_value = self.fake_today
        Profile.objects.create(
            email='user2@user.ru',
            password='smartuser2',
            birthday=date_util.today(),
        )
        for value in self.urls:
            with self.subTest('Failed to open url', value=value):
                response = self.client.get(reverse(value))
                self.assertTrue(response.context)
                self.assertIn('users', response.context)
                self.assertEqual(len(response.context['users']), 2)

    @mock.patch('core.date_util.today')
    def test_show_user_another_birthday_context(self, mock_today):
        mock_today.return_value = self.fake_today
        tomorrow = date_util.today() + timedelta(days=1)
        Profile.objects.create(
            email='user2@user.ru',
            password='smartuser2',
            birthday=tomorrow,
        )
        for value in self.urls:
            with self.subTest('Failed to open url', value=value):
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
