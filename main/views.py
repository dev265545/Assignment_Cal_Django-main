from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def index(response):
    return render(response,"main/base.html",{})
def v1(response):
    return HttpResponse("<h1>Calendar app 2</h1>")