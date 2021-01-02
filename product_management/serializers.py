from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from product_management.models import Motherboard, Ram, Ssd, Cpu, Gpu, Manage, Product

productFields = ['type_id', 'brand', 'quantity', 'price', 'product_picture', 'available']


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = productFields + ['chip', 'size', 'expansion']


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = productFields + ['gen', 'size', 'speed', 'channel']


class SsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ssd
        fields = productFields + ['interface', 'size', 'speed']


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = productFields + ['socket', 'cores', 'clock', 'cache']


class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = productFields + ['model', 'size']


class ProductSerializer(PolymorphicSerializer):
    class Meta:
        fields = productFields
        model = Product
    resource_type_field_name = 'type'
    model_serializer_mapping = {
        Motherboard: MotherboardSerializer,
        Ram: RamSerializer,
        Ssd: SsdSerializer,
        Cpu: CpuSerializer,
        Gpu: GpuSerializer
    }


class ManageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manage
        fields = ['Staff_id', 'Ptype_id']
