from django.urls import path
from . import views

urlpatterns=[

    path('', views.TestimonialsListView.as_view(), name='testimonials_list'),
    path('new/', views.CreateTestimonialsView.as_view(), name='testimonials_new'),
    path('<int:pk>/edit/', views.TestimonialsUpdateView.as_view(), name='testimonials_edit'),
    path('<int:pk>/remove/',views.TestimonialsDeleteView.as_view(), name='testimonials_remove'),
]