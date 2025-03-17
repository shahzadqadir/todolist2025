from django.urls import path

from .views import RulesTemplateView

urlpatterns = [
    path('rules/', RulesTemplateView.as_view(), name='rules'),
]