from django.urls import path
from user_management import views

urlpatterns = [
    path('', views.user_list),
    path('<str:pk>', views.user_detail),
]