from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CalculationViewTemplate(TemplateView):
    template_name = "pages/calculation.html"