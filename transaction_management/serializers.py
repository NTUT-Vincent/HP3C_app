from rest_framework import serializers

from transaction_management.models import Coupon, Order
from user_management.models import User


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['pcode', 'coupon_staff_id', 'type', 'disc_value', 'restrict']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'order_customer', 'order_staff', 'address', 'order_date_time',
                  'purchase_date_time', 'delivered_date_time', 'deliver_type', 'status']
