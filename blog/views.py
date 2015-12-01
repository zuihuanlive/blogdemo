# coding:utf-8
from django.shortcuts import render
from blog.models import *
# from datetime import date
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def globals_var(request):
    return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC}

# Create your views here.


def index(request):
    # today = date.today()
    category_list = Category.objects.all()
    article_list = Article.objects.all()
    # 分页对象，分页 每页数量
    paginator = Paginator(article_list, 1)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        article_list = paginator.page(1)

    # 返回到模板，和变量
    return render(request, 'index.html', locals())
