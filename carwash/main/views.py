from django.views.generic import TemplateView, CreateView, DetailView
from .models import Car ,Worker
from payment.models import PriceWash
from django.utils import timezone

from django.db.models import Sum



class CarsView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(CarsView, self).get_context_data(**kwargs)
        startdate = self.request.GET.get('startdate', None)
        enddate = self.request.GET.get('enddate', None)
        car_type = self.request.GET.get('cartype', 'all')
        worker = self.request.GET.get('worker', 'all')
        print(car_type)
        carwash = Car.objects.all().order_by('-id')
      
   
        
        if startdate and enddate:
            carwash = carwash.filter(created__range=[startdate + ' 00:00', enddate +' 23:59'])
            context['count_date'] = carwash.count()
            context['price_date'] = carwash.filter().aggregate(Sum('price'))
        if car_type != 'all':
            
           carwash = carwash.filter(car_type=car_type)
           context['count_type'] = carwash.count()
           context['price_type'] = carwash.filter().aggregate(Sum('price'))
        if worker != 'all':
          
          carwash = carwash.filter(worker__full_name=worker)
          context['count'] = carwash.count()
          context['price'] = carwash.filter().aggregate(Sum('price'))
         
    
        context['count_all'] = carwash.count()
        context['price_all'] = carwash.filter().aggregate(Sum('price'))
        context['cars'] = carwash
        context['startdate'] = startdate
        context['enddate'] = enddate
        context['select_car_type'] = car_type
        context['select_worker'] = worker
        context['worker_list'] = Worker.objects.all()
        context['client'] = Car.objects.all()
         

        return context


    
class AddCarsView(CreateView):
    template_name = 'add_car.html'
    model = Car
    fields = ['worker', 'car_type', 'wash_type', 'model', 'number', 'price' ]
    success_url = '/cars/'

    def get_context_data(self, **kwargs):
        context = super(AddCarsView, self).get_context_data(**kwargs)
        context['price_list'] = PriceWash.objects.all()
        return context
    def form_valid(self, form):
     form.instance.user= self.request.user
     return super(AddCarsView, self).form_valid(form)
    


class WorkerView(TemplateView):
    template_name = 'worker.html'

    def get_context_data(self, **kwargs):
        context = super(WorkerView, self).get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        return context



class CarsDetailView(DetailView):
    template_name = 'c_detail.html'
    model = Car
    context_object_name = 'cars'
    




