from django.contrib import admin
from django.urls import path
from .views import CarsView, WorkerView, AddCarsView


urlpatterns = [
    path('cars/', CarsView.as_view(), name='car'),
    path('workers', WorkerView.as_view(), name='worker'),
    path('cars/add', AddCarsView.as_view(), name='add_car'),
]