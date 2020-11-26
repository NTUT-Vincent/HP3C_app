from django.urls import path

from product_management import views

urlpatterns = [
    path('', views.product_list),
    path('id/<str:pk>/', views.product_detail),
    path('manage/', views.manage_list),
    path('manage/detail/<str:staff_id>/<str:ptype_id>/', views.manage_detail),
]
