from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('add_sprint/', views.add_sprint, name='add_sprint'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/<int:id>/', views.task, name='task'),
    path('tasks/<int:id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('add_prayer/', views.add_prayer, name='add_prayer'),
    path('add_meditation/', views.add_meditation, name='add_meditation'),
]