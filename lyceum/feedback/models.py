from django.db import models


class Feedback(models.Model):
    name = models.CharField(
        'имя',
        help_text='Максимальная длина 150',
        max_length=150,
        null=True,
    )
    email = models.EmailField(
        'почта',
        max_length=320,
        help_text='Максимум 320 символов',
        null=True,
    )
    text = models.TextField(
        'текст'
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        default_related_name = 'fback'
        verbose_name = 'Заявку на фидбек'
        verbose_name_plural = 'Заявки на фидбек'

    def __str__(self):
        return self.name
