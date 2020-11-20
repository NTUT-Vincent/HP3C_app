# Create your views here.
from rest_framework import viewsets

from user_management.serializers import UserSerializers
from user_management.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
