from django.shortcuts import render,HttpResponse,redirect
from app01.models import Article
from markdown import markdown
from django.forms import fields
from django.forms import widgets
from django import forms
from django.db import models
from app01 import models
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    post_list = Article.objects.all()
    return render(request,'index.html',{'post_list':post_list})

class FM(forms.Form):
    username = fields.CharField(
        widget = widgets.TextInput(attrs={'class':'ui input'})
    )
    pwd = fields.CharField(
        max_length=20,
        min_length=6,
        widget = widgets.PasswordInput(attrs={'class':'ui input'})
    )


def login(request):
    if request.method == 'GET':
        obj = FM()
        return render(request,'login.html',{'obj':obj})
    elif request.method =='POST':
        obj = FM(request.POST)
        r = obj.is_valid()
        if r:
            name = request.POST.get('username')
            try:
                result = models.UserInfo.objects.get(username=name)   #数据库不存在用户名可以注册
            except Exception as e:
                models.UserInfo.objects.create(**obj.cleaned_data)
                # return render(request, 'login.html', {'massage': '注册成功'})
                return HttpResponseRedirect("/index")
            else:
                return render(request, 'login.html', {'massage': '用户已存在请重新检查输入'})
        else:
            return render(request,'login.html',{'obj':obj})  #填写注册信息时页面上显示错误信息

def content_detail(request,uid):
    contents = Article.objects.get(id=uid)
    contents.content = markdown(contents.content,['codehilite'],extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    contents.increat_views()
    return render(request,'content_detail.html',{'contents':contents})

def django_url(request):
    content = Article.objects.filter(category_id=1).values()
    print(content)
    return render(request,'django.html',{'contents':content})

def ml(request):
    content = Article.objects.filter(category_id=2).values()
    return render(request,'ml.html',{'contents':content})

def python(request):
    content = Article.objects.filter(category_id=3).values()
    return render(request, 'python.html', {'contents': content})