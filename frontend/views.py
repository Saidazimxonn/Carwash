from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'    

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['salom'] = 'Salom Hammaga'
        return context