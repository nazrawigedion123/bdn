from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from .models import Comment, Subscriber
from .forms import CommentForm,SubscriberForm

#list view
class ListCommentView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Comment

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Comment.objects.all()


#create comment view

class CreateCommentView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    model = Comment
    form_class = CommentForm
    redirect_field_name = "index.html"


#delete comment view
class DeleteCommentView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('contactUs:comment_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# subscriber list view

class ListSubscriberView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    model = Subscriber

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Subscriber.objects.all()

# subscriber create view
class CreateSubscriberView(CreateView):
    redirect_field_name = 'index.html'
    form_class = SubscriberForm
    model = Subscriber  # Add this line

    def form_valid(self, form):
        return super().form_valid(form)



# subscriber delete view
class DeleteSubscriberView(LoginRequiredMixin, DeleteView):
    model = Subscriber
    success_url = reverse_lazy('contactUs:subscriber_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SuccessCommentPage(TemplateView):
    template_name = 'contactUs/success_comment.html'


class SuccessSubscriptionPage(TemplateView):
    template_name = 'contactUs/success_subscribe.html'



# Create your views here.
