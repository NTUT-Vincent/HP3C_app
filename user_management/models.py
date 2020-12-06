from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.db import models


# Create your models here.

def genderValidator(value):
    if value not in ['F', 'M']:
        raise ValidationError(
            'Gender column only can be "M" or "F".'
        )


class User(models.Model):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters are allowed.')

    user_id = models.TextField(
        primary_key=True, validators=[MinLengthValidator(3), MaxLengthValidator(12), alphanumericValidator])
    address = models.TextField()
    gender = models.TextField(validators=[genderValidator])
    name = models.TextField(validators=[MinLengthValidator(1), MaxLengthValidator(20), alphanumericValidator])
    password = models.TextField(validators=[MinLengthValidator(8), MaxLengthValidator(16), alphanumericValidator])
    user_type = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        db_table = 'USER'
