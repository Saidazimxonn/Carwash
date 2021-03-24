from django.db import models
from .choices import WASH_TYPE ,CARS_TYPE, WORKER_STATUS
from django.contrib.auth.models import User

class Worker(models.Model):

    full_name = models.CharField('Full name Worker', max_length=100)
    started_work  = models.DateField(auto_now_add=True)
    phone = models.CharField('Phone', max_length=100)
    status = models.CharField('Status worker', choices=WORKER_STATUS, default='OOW', max_length=100 )

    def __str__(self):
        return self.full_name

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(Worker,  related_name='+',  on_delete=models.CASCADE)
    car_type = models.CharField('Type cars', choices=CARS_TYPE, default='D', max_length=100)
    wash_type = models.CharField('Enter wash type', choices=WASH_TYPE, default='D', max_length=100)
    model = models.CharField('Model cars', max_length=100)
    number = models.CharField('Number cars', max_length=100 )
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.model



