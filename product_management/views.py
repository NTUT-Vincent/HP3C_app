# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
from django.db import connection
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from product_management.models import Product, Manage
from product_management.serializers import ProductSerializer, ManageSerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def product_list(request):
    """
    List all code Product, or create a new snippet.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def manage_list(request):
    """
    List all code Product, or create a new snippet.
    """
    if request.method == 'GET':
        manage = Manage.objects.all()
        serializer = ManageSerializers(manage, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ManageSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def manage_detail(request, **kwarg):
    """
    Retrieve, update or delete a code snippet.
    """
    staff_id = kwarg.get('staff_id')
    ptype_id = kwarg.get('ptype_id')
    print(staff_id)
    
    try:
        manage = Manage.objects.get(Staff_id = staff_id, Ptype_id=ptype_id)
        # manage = Manage.objects.raw("SELECT * FROM MANAGE")
    except Manage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ManageSerializers(manage)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ManageSerializers(manage, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        manage.delete()
        return HttpResponse(status=204)