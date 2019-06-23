from django.db import models
from mdeditor.fields import MDTextField,MDEditorWidget
# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=10,unique=True)
    body=MDTextField()
    def __str__(self):
        return self.name