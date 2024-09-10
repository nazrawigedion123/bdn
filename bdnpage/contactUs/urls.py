from django.urls import path
from . import views

urlpatterns =[
    path('feedbacks/', views.ListCommentView.as_view(), name='comment_list'),
    path('feedback/<int:pk>/remove/', views.DeleteCommentView.as_view(), name='comment_remove'),
    path('subscribers/', views.ListSubscriberView.as_view(), name='subscriber_list'),
    path('subscribers/<int:pk>/remove/', views.DeleteSubscriberView.as_view(), name='subscriber_remove'),

    path('success/', views.SuccessCommentPage.as_view(), name='success_comment'),
    path('successful_subscription/', views.SuccessSubscriptionPage.as_view(), name='success_subscription'),

]