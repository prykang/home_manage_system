#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.conf.urls import url
from .api import *



urlpatterns = [
    url(r'api/get_list',get_list),# 获取所有
    url(r'api/add_item',add_item),# 添加记录单元
    url(r'api/get_item',get_item),# 获得记录单元
    url(r'api/edit_item',edit_item),# 修改记录单元
    url(r'api/delete_items',delete_items),# 删除记录单元
    url(r'api/get_bankcard_type_list',get_bankcard_type_list),# 获取银行卡类型列表
    url(r'api/get_bank_list',get_bank_list),# 获取银行列表
]