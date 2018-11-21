#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.conf.urls import url
from .api import *


# 阅读管理
urlpatterns = [
    url(r'api/get_list', get_list),  # 获取所有
    url(r'api/add_item', add_item),  # 添加记录单元
    url(r'api/get_item', get_item),  # 获得记录单元
    url(r'api/edit_item', edit_item),  # 修改记录单元
    url(r'api/get_book_list', get_book_list),  # 修改记录单元
    url(r'api/add_book', add_book),  # 添加图书

    url(r'api/add_author', add_author),  # 添加作者记录单元
    url(r'api/get_author_list', get_author_list),  # 获得作者记录单元列表
    url(r'api/add_country', add_country),  # 添加国家地区记录单元
    url(r'api/get_country_list', get_country_list),  # 获得国家地区列表单元
]