from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import memes
import datetime
from django.contrib.auth.decorators import login_required




def memes_main(request):
    obj = memes.objects.all().order_by('-id')
    template_name = 'memes_main.html'
    context = {'obj':obj}

    return render(request, template_name, context)
