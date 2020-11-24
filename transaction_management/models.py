from django.db import models

# Create your models here.
from user_management.models import User


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
    address = models.TextField()
    order_date_time = models.TimeField()
    purchase_date_time = models.TimeField()
    delivered_date_time = models.TimeField()
    deliver_type = models.TextField()
    status = models.TextField()

    class Meta:
        db_table = 'ORDER'
