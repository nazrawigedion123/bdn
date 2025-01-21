from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('new/', views.vacancy_create, name='vacancy_create'),
    path('<int:pk>/delete/', views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]