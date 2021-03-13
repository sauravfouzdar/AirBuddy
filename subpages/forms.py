from django.forms import ModelForm
from .models import memes

class memesForm(ModelForm):
    class Meta:
        model = memes 
        exclude = ('created_on','author')