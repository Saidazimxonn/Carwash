from django.contrib import admin
from django.db import models
from .models import PriceWash
# Register your models here.
@admin.register(PriceWash)
class PriceWashAdmin(admin.ModelAdmin):
 pass