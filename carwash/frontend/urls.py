from django.contrib import admin
from django.urls import path
from .views import BaseView
from main.views import CarsView
from .views import BaseView, LoginView

urlpatterns = [
    path('', CarsView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login-view'),
]