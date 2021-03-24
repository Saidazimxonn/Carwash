from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from .models import Car ,Worker

class CarsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(CarsView, self).get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context
    
class AddCarsView(CreateView):
    template_name = 'add_car.html'
    model = Car
    fields = '__all__'
    success_url = '/cars/'
    
class WorkerView(TemplateView):
    template_name = 'worker.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerView, self).get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        return context