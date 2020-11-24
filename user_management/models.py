from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.TextField(primary_key=True)
    address = models.TextField()
    gender = models.TextField()
    name = models.TextField()
    password = models.TextField()
    user_type = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        db_table = 'USER'
