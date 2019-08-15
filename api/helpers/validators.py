import re
from rest_framework.serializers import ValidationError


def validate_password(password):
    if not re.match("^(?=.{4})(?=.*[A-Za-z])(?=.*[0-9])", password):
        raise ValidationError('Ensure password has a letter, a number and atleast 4 characters long')
