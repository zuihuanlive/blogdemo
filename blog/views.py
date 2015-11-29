# coding:utf-8
from django.shortcuts import render
from blog.models import *
from datetime import date

# Create your views here.


def index(request):
    today = date.today()
    articles = Article.objects.all()


    # 返回到模板，和变量
    return render(request, 'index.html', locals())