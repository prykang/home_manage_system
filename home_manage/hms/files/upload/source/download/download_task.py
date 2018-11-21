#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from importlib.machinery import SourceFileLoader
import uuid


def call_download(filename,start_url,title,author):
    print('ret')
    foo = SourceFileLoader("lib","./files/upload/source/download/"+filename).load_module()
    print('ret')
    path_filename = './files/download/fiction/' + title + str(uuid.uuid1())+'.txt'
    print('ret')
    ret = foo.download(path_filename= path_filename ,start_url=start_url,author=author)
    print('ret',ret)
    ret['file_path'] = path_filename
    print('ret', ret)
    return ret