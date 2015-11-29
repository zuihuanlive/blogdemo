# coding:utf-8
from django.db import models

# Create your models here.
# 1 django_manage.py makemigrations
# 2 django_manage.py migrate
# 3 django_manage.py createsuperuser


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author)
