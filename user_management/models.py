from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

def genderValidator(value):
    if value not in ['F', 'M']:
        raise ValidationError(
            _('%(value)s only can be "M" or "F"'),
            params={'value': value}
        )


class User(models.Model):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    user_id = models.TextField(
        primary_key=True, validators=[MinLengthValidator(3), MaxLengthValidator(10), alphanumericValidator])
    address = models.TextField()
    gender = models.TextField(validators=[genderValidator])
    name = models.TextField(validators=[MinLengthValidator(1), MaxLengthValidator(6), alphanumericValidator])
    password = models.TextField(validators=[MinLengthValidator(8), MaxLengthValidator(16), alphanumericValidator])
    user_type = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        db_table = 'USER'
