from django.urls import path

from transaction_management import views

urlpatterns = [
    path('coupon/', views.coupon_list),
    path('coupon/id/<str:pk>/', views.coupon_detail),
    path('order/', views.order_list),
    path('order/id/<str:pk>/', views.order_detail),
    path('order/price/<str:order_id>/', views.get_order_price),
    path('line_item/', views.line_item_list),
    path('line_item/<str:order_id>/', views.line_item_for_order),
]