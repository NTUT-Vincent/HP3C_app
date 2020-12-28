from django.urls import path

from product_management import views

urlpatterns = [
    path('', views.product_list),
    path('id/<str:pk>/', views.product_detail),
    path('manage/', views.manage_list),
    path('manage/detail/', views.manage_detail),
    path('type/<str:product_type>/', views.product_list_with_type),
    path('ranking/', views.product_sales_ranking),
    path('search/<str:search_string>/', views.product_search),
]
