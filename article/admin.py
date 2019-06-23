from django.contrib import admin

# Register your models here.
from .models import *
from .models import models
from mdeditor.widgets import MDEditorWidget

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{
            'widget':MDEditorWidget
        }
    }
admin.site.register(Article,BlogAdmin)