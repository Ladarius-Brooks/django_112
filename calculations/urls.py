from django.urls import path
from .views import CalculationViewTemplate


urlpatterns=[
    path('', CalculationViewTemplate.as_view(num=100), name="calc"),
]