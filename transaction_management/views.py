from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from transaction_management.models import Coupon, Order
from transaction_management.serializers import CouponSerializers


@csrf_exempt
def coupon_list(request):
    """
    List all code User, or create a new snippet.
    """
    if request.method == 'GET':
        coupon = Coupon.objects.all()
        serializer = CouponSerializers(coupon, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        coupon = JSONParser().parse(request)
        serializer = CouponSerializers(data=coupon)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def coupon_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        coupon = Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CouponSerializers(coupon)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CouponSerializers(coupon, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        coupon.delete()
        return HttpResponse(status=204)

@csrf_exempt
def order_list(request):
    """
    List all code User, or create a new snippet.
    """
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = CouponSerializers(order, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        order = JSONParser().parse(request)
        serializer = CouponSerializers(data=order)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def coupon_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CouponSerializers(order)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CouponSerializers(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204)
