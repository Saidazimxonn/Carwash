from django.db import models
from main.choices import WASH_TYPE, CARS_TYPE
class PriceWash(models.Model):
    car_type = models.CharField('Type cars', choices=CARS_TYPE, default='C', max_length=100)
    wash_type = models.CharField('Enter wash type', choices=WASH_TYPE, default='TW', max_length=100)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.car_type)

    
    

