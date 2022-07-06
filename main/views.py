from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def index(response):
    return render(response,"main/base.html",{})
