#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/7/17 10:52
# @Author  : lixiaobo
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
# @license: (C) Copyright 2018-2027, By lixiaobo.
"""


'''
from django.conf.urls import url
from home import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginVerify/$', views.loginVerify, name='loginVerify'),
    url(r'^index/$', views.index, name='index'),
]



urlpatterns = [
        url('', views.login, name='login'),
        # url(r'home/', views.login, name='login')
]
'''


from django.template.defaulttags import url
from django.conf.urls import url
from . import views


app_name = 'home'
urlpatterns = [
        url(r'^$', views.home, name='home'),
        url('^do_login/$', views.do_login, name='do_login'),
]
