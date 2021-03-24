from django.contrib import admin
from django.db import models
from .models import PriceWash
# Register your models here.
@admin.register(PriceWash)
class PriceWashAdmin(admin.ModelAdmin):
 list_display = (
     'car_type', 'wash_type', 'price'
 )
 list_display_links = (
     'car_type', 'wash_type', 'price'
 )
 list_filter = (
     'car_type', 'wash_type'
 )
