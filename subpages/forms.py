from django.forms import ModelForm
from .models import memes, confessions

class memesForm(ModelForm):
    class Meta:
        model = memes 
        exclude = ('created_on','author')


class confessionsForm(ModelForm):
    class Meta:
        model = confessions
        exclude = ('created_on','author')