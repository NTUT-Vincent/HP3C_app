from rest_framework import serializers

from user_management.models import User

class ToGenderStringCharField(serializers.CharField):
    def to_representation(self, value):
        if value == 'M':
            return 'Male'
        elif value == 'F':
            return 'Female'

class UserSerializers(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    gender = ToGenderStringCharField()
    class Meta:
        model = User
        fields = ['user_id', 'address', 'gender', 'name', 'password', 'user_type', 'type']

    def get_type(self, obj):
        if obj.user_type == 0:
            return 'visitor'
        elif obj.user_type == 1:
            return 'buyer member'
        elif obj.user_type == 2:
            return 'employee'
        elif obj.user_type == 3:
            return 'manager'
