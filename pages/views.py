from django.shortcuts import render

from django.views import generic


class RulesTemplateView(generic.TemplateView):
    template_name = 'pages/rules_list.html'
