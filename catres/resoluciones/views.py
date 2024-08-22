from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def resoluciones(requed):
    return HttpResponse("hola resoluciones")