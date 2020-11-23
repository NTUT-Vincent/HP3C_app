from django.urls import path

from product_management import views

urlpatterns = [
    path('', views.product_list),
    path('id/<str:pk>/', views.product_detail),
]
