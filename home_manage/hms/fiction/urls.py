#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.conf.urls import url
from .api import *
from .task_api import *



urlpatterns = [
    url(r'api/get_list',get_list),# 获取所有
    url(r'api/add_item',add_item),# 添加记录单元
    url(r'api/get_item',get_item),# 获得记录单元
    url(r'api/edit_item',edit_item),# 修改记录单元
    url(r'api/delete_item',delete_item),# 删除记录单元
    url(r'api/get_fiction_type_list',get_fiction_type_list),# 获取小说类型列表
    url(r'api/add_fiction_type',add_fiction_type),# 添加小说类型
    url(r'api/add_author',add_author),# 添加作者
    url(r'api/get_author_list',get_author_list),# 获取作者列表
    url(r'api/get_source_status_list',get_source_status_list),# 获取资源状态选项
    url(r'api/get_source_list',get_source_list),# 获取资源状态选项
    url(r'api/get_source',get_source),# 获取资源状态选项
    url(r'api/add_source',add_source),# 获取资源状态选项
    url(r'api/edit_source',edit_source),# 获取资源状态选项
    url(r'api/delete_source',delete_source),# 获取资源状态选项


    url(r'api/start_search_and_download',start_search_and_download),# 开始下载任务
]