from django.forms import ModelForm
from .models import memes, confessions, ml, WebDevelopment, examCorner

class memesForm(ModelForm):
    class Meta:
        model = memes 
        exclude = ('created_on','author')


class confessionsForm(ModelForm):
    class Meta:
        model = confessions
        exclude = ('created_on','author')

class mlForm(ModelForm):
    class Meta:
        model = ml
        exclude = ('created_on','author')   


class WebDevelopmentForm(ModelForm):
    class Meta:
        model = WebDevelopment
        exclude = ('created_on','author')   

class examCornerForm(ModelForm):
    class Meta:
        model = examCorner
        exclude = ('created_on','author')   
