from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator, \
    MaxLengthValidator
from django.db import models, connections


# Create your models here.

def genderValidator(value):
    if value not in ['F', 'M']:
        raise ValidationError(
            'Gender column only can be "M" or "F".'
        )


class User(models.Model):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z_]*$', 'Only alphanumeric characters are allowed.')

    user_id = models.CharField(
        max_length=22, primary_key=True, validators=[MinLengthValidator(3), alphanumericValidator])
    address = models.TextField()
    gender = models.CharField(max_length=1, validators=[genderValidator])
    name = models.CharField(max_length=20, validators=[MinLengthValidator(1), alphanumericValidator])
    password = models.CharField(
        max_length=16, validators=[MinLengthValidator(8), alphanumericValidator])
    user_type = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        db_table = 'USER'

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_user_with_id_and_password(user_id, password):
    with connections['httcs'].cursor() as cursor:
        cursor.execute("SELECT U.* FROM USER U WHERE U.user_id = '" + user_id + "'AND U.password = '" + password + "';")
        result = dictfetchall(cursor)
    print(user_id)
    print(password)
    return result