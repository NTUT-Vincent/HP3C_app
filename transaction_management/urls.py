from django.urls import path

from transaction_management import views

urlpatterns = [
    path('coupon/', views.coupon_list),
    path('coupon/id/<str:pk>/', views.coupon_detail),
]