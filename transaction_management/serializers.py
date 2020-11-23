from rest_framework import serializers

from transaction_management.models import Coupon
from user_management.models import User


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['pcode', 'staff_id', 'type', 'disc_value', 'restrict']


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['order_id', 'customer_id', 'staff_id', 'address', 'order_date_time',
                  'purchase_date_time', 'delivered_date_time', 'deliver_type', 'status']
