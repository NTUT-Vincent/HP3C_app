from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from polymorphic.models import PolymorphicModel
from rest_framework.exceptions import ValidationError
from user_management.models import User


def ProductTypeValidator(value):
    product_list = [
        'Motherboard', 'Ram', 'Ssd', 'Cpu', 'Gpu'
    ]
    if value not in product_list:
        raise ValidationError(
            'Type column only can be "Motherboard", "Ram", "Ssd", "Cpu" or "Gpu".'
        )


class Product(PolymorphicModel):
    type_id = models.CharField(max_length=30, primary_key=True)
    brand = models.CharField(max_length=20)
    quantity = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    # type = models.TextField(validators=[ProductTypeValidator])
    product_manager = models.ManyToManyField(User, through='Manage')
    product_picture = models.TextField()

    class Meta:
        db_table = 'PRODUCT'


class Motherboard(Product):
    chip = models.CharField(max_length=10)
    size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    expansion = models.TextField()

    class Meta:
        db_table = 'MB'


class Ram(Product):
    gen = models.CharField(max_length=10)
    size = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)
    channel = models.PositiveIntegerField()

    class Meta:
        db_table = 'RAM'


class Ssd(Product):
    interface = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    size = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)

    class Meta:
        db_table = 'SSD'


class Cpu(Product):
    socket = models.CharField(max_length=20)
    cores = models.PositiveIntegerField()
    clock = models.CharField(max_length=20)
    cache = models.CharField(max_length=20)

    class Meta:
        db_table = 'CPU'


class Gpu(Product):
    model = models.CharField(max_length=30)
    size = models.CharField(max_length=20)

    class Meta:
        db_table = 'GPU'


class Manage(models.Model):
    Staff_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='Staff_id')
    Ptype_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='Ptype_id')

    class Meta:
        db_table = 'MANAGE'
        unique_together = ("Staff_id", "Ptype_id")
        models.UniqueConstraint(fields = ['Staff_id', 'Ptype_id'], name = 'Manage Key')