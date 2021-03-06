from django.db import models, connections
from django.core.validators import MinValueValidator

# Create your models here.
from user_management.models import User
from product_management.models import Product


class Coupon(models.Model):
    pcode = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length = 20)
    coupon_staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='coupon_staff')
    type = models.CharField(max_length=20)
    disc_value = models.FloatField()
    restrict = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'COUPON'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order_customer')
    order_staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order_staff', null=True)
    coupon_code = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='coupon_code', null=True)
    address = models.TextField()
    order_date_time = models.DateTimeField()
    payment = models.CharField(max_length=20)
    delivered_date_time = models.DateTimeField(null=True)
    deliver_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'PURCHASE_ORDER'


class LineItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    type_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='type_id')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'LINE_ITEM'
        unique_together = ("order_id", "type_id")
        # models.UniqueConstraint(fields = ['Staff_id', 'Ptype_id'], name = 'Manage Key')


def get_line_item_by_order(order_id):
    with connections['httcs'].cursor() as cursor:
        cursor.execute("SELECT order_id, type_id, quantity FROM LINE_ITEM WHERE order_id = %s", [order_id])
        result = dictfetchall(cursor)
    result = [
        {
            'order_id': r['order_id'],
            'type_id': r['type_id'],
            'quantity': r['quantity']
        }
        for r in result
    ]
    return result


def get_price_of_order(order_id):
    with connections['httcs'].cursor() as cursor:
        cursor.execute("SELECT O.price FROM ORDER_WITH_PRICE O WHERE order_id = %s", [order_id])
        result = dictfetchall(cursor)
        result[0]['price'] = round(result[0]['price'])
    print(result)
    return result

def get_order_of_user(user_id):
    with connections['httcs'].cursor() as cursor:
        cursor.execute("SELECT * FROM ORDER_WITH_PRICE O WHERE O.order_customer_id = %s", [user_id])
        result = dictfetchall(cursor)
        # result[0]['price'] = round(result[0]['price'])
    print(result)
    for x in result:
        x['items'] = get_line_item_by_order(x['order_id'])
    return result

def get_revenue(start_date, end_date):
    with connections['httcs'].cursor() as cursor:
        cursor.execute("SELECT sum(O.price) AS revenue\
                        FROM ORDER_WITH_PRICE O \
                        WHERE O.order_date_time BETWEEN %s and %s", [start_date, end_date])
        result = dictfetchall(cursor)
        result[0]['revenue'] = round(result[0]['revenue'])
    print(result)
    return result

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
