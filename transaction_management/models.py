from django.db import models

# Create your models here.
from user_management.models import User


class Coupon(models.Model):
    pcode = models.TextField(primary_key=True)
    coupon_staff = models.ForeignKey(
        User, models.CASCADE, related_name='coupon_staff', limit_choices_to={'type': [2, 3]})
    type = models.TextField()
    disc_value = models.TextField()
    restrict = models.TextField()

    class Meta:
        db_table = 'COUPON'


class Order(models.Model):
    order_id = models.TextField(primary_key=True)
    order_customer = models.ForeignKey(
        User, models.CASCADE, related_name='order_customer', limit_choices_to={'type': 1})
    order_staff = models.ForeignKey(
        User, models.CASCADE, related_name='order_staff', limit_choices_to={'type': [2, 3]})
    address = models.TextField()
    order_date_time = models.TimeField()
    purchase_date_time = models.TimeField()
    delivered_date_time = models.TimeField()
    deliver_type = models.TextField()
    status = models.TextField()

    class Meta:
        db_table = 'ORDER'
