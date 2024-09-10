from django.urls import path
from . import views

urlpatterns=[

    path('', views.PersonnelListView.as_view(), name='personnel_list'),
    path('new/', views.PersonnelCreateView.as_view(), name='personnel_new'),
    path('<int:pk>/edit/', views.PersonnelUpdateView.as_view(), name='personnel_edit'),
    path('<int:pk>/remove/',views.PersonnelDeleteView.as_view(), name='personnel_remove'),
]