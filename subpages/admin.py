from django.contrib import admin
from .models import memes, confessions, ml, WebDevelopment, examCorner
# Register your models here.
admin.site.register(memes)
admin.site.register(confessions)
admin.site.register(examCorner)
admin.site.register(WebDevelopment)
admin.site.register(ml)
