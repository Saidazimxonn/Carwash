from django.urls import path
from .views import CarsView, WorkerView, AddCarsView, CarsDetailView


urlpatterns = [

    path('cars/', CarsView.as_view(), name='car'),
    path('workers', WorkerView.as_view(), name='worker'),
    path('cars/add', AddCarsView.as_view(), name='add_car'),
    path('car/detail/<int:pk>/', CarsDetailView.as_view(), name='car_detail'),
]

