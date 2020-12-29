from django.urls import path
from user_management import views

urlpatterns = [
    path('', views.user_list),
    path('<str:pk>', views.user_detail),
    path('login/<str:id>/<str:password>/', views.user_login),
]