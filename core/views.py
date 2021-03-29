from __future__ import unicode_literals
from django.shortcuts import render, redirect
from itertools import chain
from subpages.models import memes, confessions, ml, WebDevelopment, examCorner

# Create your views here.
def home(request):
    template_name =  'index.html' 
    object_list = sorted(chain(
        memes.objects.all(),
        confessions.objects.all(),
        ml.objects.all()
    ), key=lambda obj: obj.created_on)

    return render(request, template_name, {'feed': object_list})

def profile(request):
    obj = memes.objects.all().order_by('-id')
    template_name =  'user_profile.html' 
    context = {'obj':obj}
    return render(request, template_name, context)    

def main_submit(request):
    template_name =  'main_submit.html' 
    context = {}
    return render(request, template_name, context)    