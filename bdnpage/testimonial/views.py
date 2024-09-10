from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, )
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Testimonials
from .forms import TestimonialsForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# Create your views here.

class TestimonialsListView(ListView):
    model = Testimonials

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Testimonials.objects.all()


class CreateTestimonialsView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'testimonial/testimonials_list.html'
    form_class = TestimonialsForm
    model = Testimonials  # Add this line

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class TestimonialsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'testimonial/testimonials_list.html'
    form_class = TestimonialsForm
    model = Testimonials

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TestimonialsDeleteView(LoginRequiredMixin, DeleteView):
    model = Testimonials
    success_url = reverse_lazy('testimonial:testimonials_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
