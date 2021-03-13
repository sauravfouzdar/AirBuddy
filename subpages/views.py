from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import memes, confessions
import datetime
from .forms import memesForm, confessionsForm
from django.contrib.auth.decorators import login_required


def memes_main(request):
    obj = memes.objects.all().order_by('-id')
    template_name = 'memes_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

@login_required
def memes_create(request):
    template_name = 'memes_create.html'
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


@login_required
def confessions_main(request):
    obj = confessions.objects.all().order_by('-id')
    template_name = 'confessions_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

@login_required
def confession_body(request,pk):
    obj = confessions.objects.get(pk=pk)
    template_name = 'confessions_body.html'
    context = {
        'body':obj.post_data,
        'title':obj.title,
        'date':obj.created_on,
    }

    return render(request, template_name, context)

@login_required
def confession_create(request):
    template_name = 'confessions_create.html'
    form = confessionsForm()
    context = {'form':form}
    if request.method == 'POST':
        form = memesForm(request.POST, request.FILES)   
        if form.is_valid():
            obj.save()
            return redirect(confessions_main)
    return render(request, template_name, context)   


