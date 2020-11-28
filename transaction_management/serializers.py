from rest_framework import serializers

from transaction_management.models import Coupon, Order, LineItem
from user_management.models import User


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['pcode', 'coupon_staff', 'type', 'disc_value', 'restrict']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'order_customer', 'order_staff', 'coupon_code','address', 'order_date_time',
                  'purchase_date_time', 'delivered_date_time', 'deliver_type', 'status']

class LineItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ['order_id', 'type_id', 'quantity']