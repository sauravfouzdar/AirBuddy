from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import memes, confessions, ml, WebDevelopment, examCorner

class memesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = memes 
        exclude = ('created_on','author')
        fields = ('author','title', 'post_data', 'created_on')
        labels = {
            'title': _('Title'),
        }


class confessionsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = confessions
        exclude = ('created_on',)

class mlForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = ml
        exclude = ('created_on','author')   


class WebDevelopmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = WebDevelopment
        exclude = ('created_on','author')   

class examCornerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = examCorner
        exclude = ('created_on','author')   
