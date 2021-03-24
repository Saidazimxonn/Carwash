from django.db import models
from main.choices import WASH_TYPE, CARS_TYPE
class PriceWash(models.Model):
    worker = models.ForeignKey('main.Worker', on_delete=models.CASCADE, verbose_name='Worker')
    car = models.ForeignKey('main.Car', on_delete=models.CASCADE, verbose_name='Cars')
    Time = models.TimeField('Time')
    Data = models.DateField('Data')
    car_type = models.CharField('Type cars', choices=CARS_TYPE, default='C', max_length=100)
    wash_type = models.CharField('Enter wash type', choices=WASH_TYPE, default='TW', max_length=100)
    
    def __str__(self):
        return str(self.worker)

    
    

