from django.db import models
from .choices import WASH_TYPE ,CARS_TYPE, WORKER_STATUS

class Car(models.Model):
    model = models.CharField('Model cars', max_length=100)
    color = models.CharField('Color cars', max_length=100)
    number = models.CharField('Number cars', max_length=100 )
    car_type = models.CharField('Type cars', choices=CARS_TYPE, default='C', max_length=100)
    wash_type = models.CharField('Enter wash type', choices=WASH_TYPE, default='TW', max_length=100)

    def __str__(self):
        return self.model

class Worker(models.Model):
    full_name = models.CharField('Full name Worker', max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_type = models.CharField('Car type', max_length=100)
    wash_type = models.CharField('Type wash', max_length=100)
    status = models.CharField('Status worker', choices=WORKER_STATUS, default='OOW', max_length=100 )

    def __str__(self):
        return self.full_name


