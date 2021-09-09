from django.core.exceptions import ValidationError


def validate_price(value):
    """
    Validate if user enter correct price
    """
    try:
        int(value)
    except ValueError:
        raise ValidationError(f'{value} is not valid price!')
