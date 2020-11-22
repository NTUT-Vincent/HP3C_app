from django.urls import path

from product_management import views

urlpatterns = [
    path('', views.product_list),
]
