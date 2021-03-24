from django.contrib import admin
from .models import Worker, Car
# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass