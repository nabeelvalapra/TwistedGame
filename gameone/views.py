from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def roundone(request):
    HttpResponse('Yeah you got it.')