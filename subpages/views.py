from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import memes, confessions, ml, WebDevelopment, examCorner
import datetime
from .forms import memesForm, confessionsForm, mlForm, WebDevelopmentForm, examCornerForm
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
        form = confessionsForm(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return redirect(confessions_main)
    return render(request, template_name, context)   


###########

@login_required
def ml_main(request):
    obj = ml.objects.all().order_by('-id')
    template_name = 'ml_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

@login_required
def ml_body(request,pk):
    obj = ml.objects.get(pk=pk)
    template_name = 'ml_body.html'
    context = {
        'body':obj.description,
        'title':obj.title,
        'date':obj.created_on,
        'author':obj.author
    }

    return render(request, template_name, context)

@login_required
def ml_create(request):
    template_name = 'ml_create.html'
    form = mlForm()
    context = {'form':form}
    if request.method == 'POST':
        form = mlForm(request.POST, request.FILES)   
        if form.is_valid():
            obj = form.save(commit = False) 
            obj.author = request.user 
            obj.save()
            return redirect(ml_main)
    return render(request, template_name, context)  

######
    
@login_required
def webd_main(request):
    obj = WebDevelopment.objects.all().order_by('-id')
    template_name = 'webd_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

@login_required
def webd_body(request,pk):
    obj = WebDevelopment.objects.get(pk=pk)
    template_name = 'webd_body.html'
    context = {
        'body':obj.description,
        'title':obj.title,
        'date':obj.created_on,
        'author':obj.author
    }

    return render(request, template_name, context)

@login_required
def webd_create(request):
    template_name = 'webd_create.html'
    form = WebDevelopmentForm()
    context = {'form':form}
    if request.method == 'POST':
        form = WebDevelopmentForm(request.POST, request.FILES)   
        if form.is_valid():
            obj = form.save(commit = False) 
            obj.author = request.user 
            obj.save()
            return redirect(webd_main)
    return render(request, template_name, context)   

####
def examCorner_main(request):
    obj = examCorner.objects.all().order_by('-id')
    template_name = 'examCorner_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)

@login_required
def examCorner_create(request):
    template_name = 'examCorner_create.html'
    form = examCornerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = examCornerForm(request.POST, request.FILES)   
        if form.is_valid():
            obj = form.save(commit = False) 
            obj.author = request.user 
            obj.save()
            return redirect(examCorner_main)
    return render(request, template_name, context) 



@login_required
def examCorner_body(request,pk):
    obj = examCorner.objects.get(pk=pk)
    template_name = 'examCorner_body.html'
    context = {
        'body':obj.description,
        'title':obj.title,
        'date':obj.created_on,
        'author':obj.author,
        'post_data':obj.post_data,
    }

    return render(request, template_name, context)


