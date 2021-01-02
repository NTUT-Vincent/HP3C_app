from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connections

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from transaction_management.models import Coupon, Order, LineItem, get_line_item_by_order, get_price_of_order, get_order_of_user, get_revenue
from transaction_management.serializers import CouponSerializers, OrderSerializers, LineItemSerializers


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
        serializer = OrderSerializers(order, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        order = JSONParser().parse(request)
        serializer = OrderSerializers(data=order)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def order_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializers(order)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializers(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204)

@csrf_exempt
def get_order_price(request, order_id):
    if request.method == 'GET':
        price = get_price_of_order(order_id)
        return JsonResponse(price, safe=False)


@csrf_exempt
def line_item_list(request):
    """
    List all code User, or create a new snippet.
    """
    if request.method == 'GET':
        line_item = LineItem.objects.all()
        serializer = LineItemSerializers(line_item, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        line_item = JSONParser().parse(request)
        serializer = LineItemSerializers(data=line_item)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def line_item_for_order(request, order_id):

    if request.method == 'GET':
        line_item = get_line_item_by_order(order_id)
        return JsonResponse(line_item, safe=False)
    elif request.method == 'DELETE':
        line_item = LineItem.objects.raw("SELECT * FROM LINE_ITEM WHERE order_id = %s", [order_id])
        for l in line_item:
            l.delete()
        return HttpResponse(status=204)

@csrf_exempt
def get_order_list_by_user(request, user_id):

    if request.method == 'GET':
        order = get_order_of_user(user_id)
        return JsonResponse(order, safe=False)

@csrf_exempt
def get_revenue_by_date(request, start_date, end_date):

    if request.method == 'GET':
        price = get_revenue(start_date, end_date)
        return JsonResponse(price, safe=False)
   


