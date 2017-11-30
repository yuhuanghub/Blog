from django.shortcuts import render,HttpResponse,redirect
from app01.models import Article
# Create your views here.

def index(request):
    post_list = Article.objects.all()
    return render(request,'index.html',{'post_list':post_list})

def login(request):
    return render(request,'login.html')

def content_detail(request,uid):
    contents = Article.objects.filter(id=uid).values()
    #print(contents)
    return render(request,'content_detail.html',{'contents':contents[0]})

def django_url(request):
    content = Article.objects.filter(category_id=1).values()
    return render(request,'django.html',{'contents':content})

def ml(request):
    content = Article.objects.filter(category_id=2).values()
    return render(request,'ml.html',{'contents':content})

def python(request):
    content = Article.objects.filter(category_id=3).values()
    return render(request, 'python.html', {'contents': content})