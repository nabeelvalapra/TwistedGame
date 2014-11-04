from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse

# Create your views here.

def roundone(request):
    return render_to_response('gameone/roundone.html')