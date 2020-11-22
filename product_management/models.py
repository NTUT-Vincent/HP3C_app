from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from polymorphic.models import PolymorphicModel


class Product(PolymorphicModel):
    type_id = models.TextField(primary_key=True)
    brand = models.TextField(max_length=20)
    quantity = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    type = models.TextField()

    class Meta:
        db_table = 'PRODUCT'


class Motherboard(Product):
    chip = models.TextField(max_length=10)
    size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    expansion = models.TextField()

    class Meta:
        db_table = 'MB'


class Ram(Product):
    gen = models.TextField(max_length=10)
    size = models.TextField()
    speed = models.TextField()
    channel = models.PositiveIntegerField()

    class Meta:
        db_table = 'RAM'


class Ssd(Product):
    interface = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    size = models.TextField()
    speed = models.TextField()

    class Meta:
        db_table = 'SSD'


class Cpu(Product):
    socket = models.TextField()
    cores = models.PositiveIntegerField()
    clock = models.TextField()
    cache = models.TextField()

    class Meta:
        db_table = 'CPU'


class Gpu(Product):
    model = models.TextField()
    size = models.TextField()

    class Meta:
        db_table = 'GPU'
