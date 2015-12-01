# coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField

# Create your models here.
# 1 django_manage.py makemigrations
# 2 django_manage.py migrate
# 3 django_manage.py createsuperuser


class User(AbstractUser):
    """
    用户
    采用继承方式扩展用户信息
    qq可以为空，号码可以为空但是不能重复
    """
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200)
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=30, verbose_name='表签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=99, verbose_name='分类排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=200, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = UEditorField(u'内容   ', width=600, height=300, toolbars="full", imagePath="images/", filePath="",
                           upload_settings={"imageMaxSize": 1204000}, settings={}, command=None,
                           blank=True)
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='作者')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户名')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)


class Links(models.Model):
    """
    链接
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='URL地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排序，从小到达')

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


class Ad(models.Model):
    """
    广告
    """
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200, verbose_name='广告语')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序，从小到达')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


# class Host(models.Model):
#     hid = models.AutoField(primary_key=True)
#     aliases = models.CharField(max_length=200)
#     ip = models.CharField(max_length=100)
#
#
# class Password(models.Model):
#     user = models.CharField(max_length=100)
#     encrypt = models.CharField(max_length=100)
#     passwd = models.CharField(max_length=100)
#     host = models.ForeignKey(Host)
