from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('add_sprint/', views.add_sprint, name='add_sprint'),
    path('add_prayer/', views.add_prayer, name='add_prayer'),
    path('add_meditation/', views.add_meditation, name='add_meditation'),
]