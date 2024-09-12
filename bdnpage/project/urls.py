from django.urls import path
from . import views

urlpatterns=[

    path('list/', views.ProjectListView.as_view(), name='project_list'),
    path('new/', views.CreateProjectView.as_view(), name='project_new'),
    path('<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/remove/',views.ProjectDeleteView.as_view(), name='project_remove'),

    path('',views.projects,name='projects')
]