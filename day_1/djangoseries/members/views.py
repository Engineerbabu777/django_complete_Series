from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):
    template = loader.get_template("First.html")
    return HttpResponse(template.render())
