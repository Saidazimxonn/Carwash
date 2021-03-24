from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import  redirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

class BaseView(TemplateView):
    template_name = 'base.html'    

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['salom'] = 'Salom Hammaga'
        return context


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'back_url' in request.POST:
                        return redirect(request.POST['back_url'])
                    return redirect(reverse('base'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')