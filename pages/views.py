from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/aboutme.html"

# Create your views here.
#def view_function(request):
   # html = "<h1>Hello, World!</h1>"
   # return HttpResponse(html)