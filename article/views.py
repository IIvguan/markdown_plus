from django.shortcuts import render
from mdeditor.fields import MDTextFormField
# Create your views here.
from django import forms
from django.views.generic import View
from .models import Article
from django.shortcuts import HttpResponse,redirect
from django.http import HttpResponseNotFound
import markdown

class BlogForm(forms.Form):
    content=MDTextFormField()

class Blog(View):
    def get(self,request):
        form=BlogForm()
        if request.GET.get('action',''):
            blog_id=int(request.GET.get('id',''))
            blog= Article.objects.get(pk=blog_id)
            return render(request,'blog.html',locals())

        return render(request,'blog.html',locals())

    def post(self,request):
        print(request.POST)
        title=request.POST.get('title')
        content=request.POST.get('content')
        Article.objects.update_or_create(name=title,body=content)
        return redirect('/list')
class BlogListView(View):
    def get(self,request):
        blog_list=Article.objects.all()
        return render(request,'list.html',locals())

def blog_detail(request,blog_id):
    try:
        blog=Article.objects.get(pk=int(blog_id))
    except:
        return HttpResponseNotFound
    blog.body=markdown.markdown(blog.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form=BlogForm()
    return render(request,'detail.html',{'blog':blog,'form':form})

