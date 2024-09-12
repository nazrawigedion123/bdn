from django.urls import path
from . import views

urlpatterns=[

    path('', views.PackageListView.as_view(), name='package_list'),
    path('new/', views.CreatePackageView.as_view(), name='package_new'),
    path('<int:pk>/edit/', views.PackageUpdateView.as_view(), name='package_edit'),
    path('<int:pk>/remove/',views.PackageDeleteView.as_view(), name='package_remove'),

    path('feature/', views.FeatureListView.as_view(),name='feature_list'),
    path('feature/new/', views.CreateFeatureView.as_view(),name='feature_new'),
    path('feature/<int:pk>/edit', views.FeatureUpdateView.as_view(),name='feature_edit'),
    path('feature/<int:pk>/delete', views.FeatureDeleteView.as_view(),name='feature_remove'),


    path('orders/', views.OrderListView.as_view(),name='order_list'),
    path('order/<int:pk>/new/', views.CreateOrderView.as_view(),name='order_new'),
    path('order/<int:pk>/edit', views.OrderUpdateView.as_view(),name='order_edit'),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view(),name='order_remove'),
    path('order/submitted/', views.OrderSubmittedView.as_view(), name='order_submitted'),
    path('notifications/', views.NotificationListView.as_view(), name='notifications_list'),

    path('create_custom/', views.create_custom, name='create_custom'),
    path('create_order/<int:custom_id>/', views.create_order, name='create_order'),
]