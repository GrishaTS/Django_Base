from django.shortcuts import reverse
from django.test import Client, TestCase

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_name_label(self):
        name_label = self.form.fields['name'].label
        self.assertEquals(name_label, 'Имя')

    def test_name_help_text(self):
        name_help_text = self.form.fields['name'].help_text
        self.assertEquals(name_help_text, 'Максимальная длина 150')

    def test_create_task(self):
        feedbacks_count = Feedback.objects.count()
        form_data = {
            'name': 'aИмя',
            'email': 'example@gmail.com',
            'text': 'ТЕКСТ ТЕСТА',
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(Feedback.objects.count(), feedbacks_count + 1)
        self.assertTrue(
            Feedback.objects.filter(
                name='aИмя',
            ).exists()
        )

    def test_item_list_page_show_correct_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)
        self.assertEqual(len(list(response.context['form'])), 3)
