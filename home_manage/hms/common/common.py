#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

import inspect
from rest_framework.authtoken.models import Token
from django.http import  JsonResponse


#获取当前运行的函数的名称
def get_current_function_name():
    return inspect.stack()[1][3]


# # 装饰器
# def authorized(func):
#     def wrapper(*args, **kw):
#         # print 'call %s():' % func.__name__
#         request = args[0]
#         if not request.user.is_authenticated():
#             return JsonResponse(
#                 {
#                     'error': '400002',
#                     'msg': 'token 无效或已过期！'
#                 },
#                 status=401)
#         else:
#             return func(*args, **kw)
#     return wrapper