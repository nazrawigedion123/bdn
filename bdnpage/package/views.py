from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, )
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Package, Feature, Order, Notification, Custom
from .forms import PackageForm, FeatureForm, OrderForm,CustomForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User, Group


# Create your views here.

class PackageListView(ListView):
    model = Package

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Package.objects.all()


class CreatePackageView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/package_list.html'
    form_class = PackageForm
    model = Package # Add this line

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class PackageUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/package_list.html'
    form_class = PackageForm
    model = Package

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PackageDeleteView(LoginRequiredMixin, DeleteView):
    model = Package
    success_url = reverse_lazy('package:package_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)







class FeatureListView(LoginRequiredMixin,ListView):
    model = Feature

    def get_queryset(self):
        return Feature.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)




class CreateFeatureView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/feature_list.html'
    form_class = FeatureForm
    model = Feature  # Add this line

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/feature_list.html'
    form_class = FeatureForm
    model = Feature

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FeatureDeleteView(LoginRequiredMixin, DeleteView):
    model = Feature
    success_url = reverse_lazy('package:feature_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OrderListView(LoginRequiredMixin,ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)




class CreateOrderView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/order_submitted.html'
    form_class = OrderForm
    model = Order  # Add this line

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):


        form.instance.package = Package.objects.get(pk=self.kwargs['pk'])
        order = form.save()

        users_to_notify = User.objects.filter(is_superuser=True)

        message = f"New order from {self.request.user.username} for package {order.package.name}"

        for user in users_to_notify:
            Notification.objects.create(
                user=user,  # Notify each user in the list
                order=order,
                message=message
            )
        return redirect(reverse('package:order_submitted'))

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'package/order_list.html'
    form_class = OrderForm
    model = Order

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('package:order_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class OrderSubmittedView(TemplateView):
    template_name = 'package/order_submitted.html'

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'package/notifications.html'

    def get_queryset(self):
        # Get unread notifications for the logged-in user

        # Get unread notifications
        notifications = Notification.objects.filter(user=self.request.user).order_by('-created_at')

        # Mark all notifications as read
        notifications.update(is_read=True)
        return notifications
# def create_custom(request):
#     if request.method == "POST":
#         form = CustomForm(request.POST)
#         if form.is_valid():
#             custom = form.save()
#             # Redirect to the order creation view with the custom id
#             return redirect(reverse('package:create_order', kwargs={'custom_id': custom.id}))
#     else:
#         form = CustomForm()
#     return render(request, 'package/customize.html', {'form': form})


def create_custom(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            custom = Custom.objects.create()

            # Save selected features for each package
            for field in form.cleaned_data:
                if field.startswith('package_'):
                    selected_features = form.cleaned_data[field]
                    custom.feature.add(*selected_features)

            custom.save()
            return redirect(reverse('package:create_order', kwargs={'custom_id': custom.id}))
    else:
        form = CustomForm()

    return render(request, 'package/customize.html', {'form': form})

def create_order(request, custom_id=None):
    custom = Custom.objects.get(id=custom_id) if custom_id else None

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.custom = custom  # Associate the order with the custom object
            order.save()

            users_to_notify = User.objects.filter(is_superuser=True)

            message = f"New order from {request.user.username} for features {order.custom.feature.all()}"

            for user in users_to_notify:
                Notification.objects.create(
                    user=user,  # Notify each user in the list
                    order=order,
                    message=message
                )
            return redirect('package:order_submitted')  # Redirect to a success page or another desired location
    else:
        form = OrderForm()

    return render(request, 'package/order_form.html', {'form': form, 'custom': custom})