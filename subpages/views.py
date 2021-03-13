from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import memes
import datetime
from .forms import memesForm
from django.contrib.auth.decorators import login_required


def memes_main(request):
    obj = memes.objects.all().order_by('-id')
    template_name = 'memes_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

def memes_create(request):
    template_name = 'memes_create.html'
    #print(memes.author)
    form = memesForm()
    context = {'form':form}
    if request.method == 'POST':
        form = memesForm(request.POST, request.FILES)   
        if form.is_valid():
            obj = form.save(commit = False) 
            obj.author = request.user 
            obj.save()
            return redirect(memes_main)
    return render(request, template_name, context)

