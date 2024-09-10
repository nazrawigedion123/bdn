from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, )
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Personnel
from .forms import PersonnelForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# Create your views here.

class PersonnelListView(ListView):
    model = Personnel

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Personnel.objects.all()


class PersonnelCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'personnel/personnel_list.html'
    form_class = PersonnelForm
    model = Personnel # Add this line

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class PersonnelUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'personnel/personnel_list.html'
    form_class = PersonnelForm
    model = Personnel

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PersonnelDeleteView(LoginRequiredMixin, DeleteView):
    model = Personnel
    success_url = reverse_lazy('personnel:personnel_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
