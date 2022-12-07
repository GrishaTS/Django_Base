from string import punctuation

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustBeParam:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        cleaned_value = value.lower()
        for i in punctuation:
            cleaned_value = cleaned_value.replace(i, ' ')
        cleaned_value = cleaned_value.split()
        if not set(self.words).intersection(set(cleaned_value)):
            raise ValidationError(
                'Текст не включает в себя "превосходно" или "роскошно"'
            )
        return value
