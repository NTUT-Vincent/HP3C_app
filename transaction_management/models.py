from django.db import models, connections
from django.core.validators import MinValueValidator

# Create your models here.
from user_management.models import User
from product_management.models import Product


class Coupon(models.Model):
    pcode = models.TextField(primary_key=True)
    coupon_staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='coupon_staff')
    type = models.TextField()
    disc_value = models.TextField()
    restrict = models.TextField()

    class Meta:
        db_table = 'COUPON'


class Order(models.Model):
    order_id = models.TextField(primary_key=True)
    order_customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order_customer')
    order_staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='order_staff')
    coupon_code = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='coupon_code')
    address = models.TextField()
    order_date_time = models.TimeField()
    purchase_date_time = models.TimeField()
    delivered_date_time = models.TimeField()
    deliver_type = models.TextField()
    status = models.TextField()

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
        cursor.execute( "SELECT  sum(P.price*L.quantity) AS price_of_order " + 
                        "FROM  PURCHASE_ORDER O, LINE_ITEM L, PRODUCT P " + 
                        "WHERE O.order_id = L.order_id AND L.type_id = P.type_id " +
                        "AND O.order_id = %s", [order_id])
        result = dictfetchall(cursor)
        price = result[0]['price_of_order']
    print(price)
    return result

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]