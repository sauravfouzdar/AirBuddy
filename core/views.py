from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    template =  'index.html' 
    return render(request, template)