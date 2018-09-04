"""
作者    ：Jimingpeng
创建时间：2018/8/31  11:33 
"""

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
