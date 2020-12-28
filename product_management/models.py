from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models, connections

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

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_product_with_type(input_type):
    with connections['httcs'].cursor() as cursor:
        if input_type.lower() == 'cpu':
            cursor.execute("SELECT * FROM PRODUCT_CPU")
        elif input_type.lower() == 'gpu':
            cursor.execute("SELECT * FROM PRODUCT_GPU")
        elif input_type.lower() == 'motherboard':
            cursor.execute("SELECT * FROM PRODUCT_MB")
        elif input_type.lower() == 'ram':
            cursor.execute("SELECT * FROM PRODUCT_RAM")
        elif input_type.lower() == 'ssd':
            cursor.execute("SELECT * FROM PRODUCT_SSD")
        
        result = dictfetchall(cursor)
    return result

def get_sales_ranking():
    with connections['httcs'].cursor() as cursor:
        cursor.execute('SELECT 	L.type_id, sum(L.quantity) AS Sales_volume\
                        FROM    LINE_ITEM L\
                        WHERE 	L.type_id  IN ( SELECT  P.type_id\
											    FROM	PRODUCT P)\
                        GROUP BY L.type_id\
                        ORDER BY Sales_volume DESC;')
        result = dictfetchall(cursor)
    return result

def search_product(search_string):
    with connections['httcs'].cursor() as cursor:
        cursor.execute('SELECT * \
                        FROM	PRODUCT P\
                        WHERE P.type_id like \'%' + search_string + '%\'')
        result = dictfetchall(cursor)
    return result

