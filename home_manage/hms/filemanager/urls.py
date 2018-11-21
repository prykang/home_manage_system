#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from django.conf.urls import url
from .api import *

urlpatterns = [
    # url(r'^test/',csrf_exempt(test),name='test'),
    # api部分

    # url(r'^api/download_module_file', download_module_file),  # 获取模版文件


    url(r'^api/upload_file', upload_file),  # 上传用例
    url(r'^api/upload_download_script_file', upload_download_script_file),  # 上传下载脚本
    url(r'^api/upload_search_script_file', upload_search_script_file),  # 上传搜索脚本
    url(r'^api/parse_file', parse_file),  # 解析文件
    url(r'^api/generate_testcase', generate_testcase),  # 生成文件

]
