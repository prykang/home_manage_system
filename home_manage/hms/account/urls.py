#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.conf.urls import url
from .api import *

urlpatterns = [
    # url(r'^test/',csrf_exempt(test),name='test'),
    # api部分
    url(r'api/registe$',registe),# 注册
    url(r'api/login$',login),# 登录
    url(r'api/logout',logout),# 登出
    url(r'api/get_userinfo$',get_userinfo),# 获取用户信息
    url(r'api/get_user_list',get_user_list),# 获取用户信息
]