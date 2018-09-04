from django.db import models
from django.contrib.auth.models import User


# Cre ate your models here.
from django.urls import reverse


class Category(models.Model):
    """ 分类"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ 标签 """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """ 文章 """
    title = models.CharField(max_length=70)                             # 标题
    body = models.TextField()                                           # 正文
    created_time = models.DateTimeField()                               # 创建时间
    modified_time = models.DateTimeField()                              # 最后一次修改时间
    excerpt = models.CharField(max_length=200, blank=True)             # 摘要 - 允许空值
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    # 分类 - 一对多的关联关系
    tags = models.ManyToManyField(Tag, blank=True)                     # 标签 - 多对多的关系，允许空值
    author = models.ForeignKey(User, on_delete=models.CASCADE)          # 内置用户 - 一对多关系

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

    def get_absolute_url(self):
        # 对应 urls 下的 name='detail'
        return reverse('blog:detail', kwargs={'pk': self.pk})
