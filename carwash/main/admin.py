from django.contrib import admin
from .models import Worker, Car
# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
   list_display = (
       'worker', 'car_type', 'wash_type', 'model', 'number', 'user'
   )
   list_display_links = (
       'worker', 'car_type', 'wash_type', 'model', 'number', 'user'
   )

   list_filter = (
        'worker', 'car_type', 'wash_type', 'model'
    )
   