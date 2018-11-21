#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane


from importlib.machinery import SourceFileLoader


def call_search(filename,keyword,author):
    foo = SourceFileLoader("lib","./files/upload/source/search/"+filename).load_module()
    ret = foo.search_fiction(keyword=keyword,author=author)
    return ret