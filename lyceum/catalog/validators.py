from functools import wraps
from string import punctuation

from django.core.exceptions import ValidationError


def validate_must_be_param(*must_be_in_our_item):
    @wraps(validate_must_be_param)
    def validator(value):
        cleaned_value = value.lower()
        for i in punctuation:
            cleaned_value = cleaned_value.replace(i, ' ')
        cleaned_value = cleaned_value.split()
        if not set(must_be_in_our_item).intersection(set(cleaned_value)):
            raise ValidationError('Текст не включает в себя "превосходно" '
                                  'или "роскошно"')
        return value
    return validator
