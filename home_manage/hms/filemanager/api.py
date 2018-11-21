#-*- coding: UTF-8 -*-
# @Author  : countofdane
# @Email   : countofdane@163.com
# @Blog    ：https://blog.csdn.net/countofdane

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import  JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from common.common import *
from common.filehandler import *
from django.core.serializers import serialize
import re
import os
import uuid



# 过滤等级和标签
#  条件是 version  module
@api_view(['POST'])
@csrf_exempt
def upload_file(request):
    try:
        if request.user.is_authenticated():
            if 'filename' in request.data:
                file = request.FILES.get("filename", None)
                if  file:
                    print(file.name)
                    # todo 这里可以增加文件格式校验
                    # 需要考虑处理文件重名的考虑
                    file_name = file.name.split('.')[0] + str(uuid.uuid1()).replace('-','') +'.'+ file.name.split('.')[1]
                    pathname = os.path.join('./files/upload', file_name)
                    print(pathname)
                    with open(pathname, 'wb+') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)

                    return JsonResponse(
                            {
                                'data':{
                                    'filename': file_name
                                },
                                'code': '000000',
                                'msg': '上传文件成功'
                            },
                            status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400000',
                            'msg': '上传文件失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'filename': 'This field is required.',
                        },
                        'code': '400001',
                        'msg': '上传文件失败'
                    },
                    status=200)

        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)

    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)



# 过滤等级和标签
#  条件是 version  module
@api_view(['POST'])
@csrf_exempt
def upload_search_script_file(request):
    try:
        if request.user.is_authenticated():
            if 'filename' in request.data:
                file = request.FILES.get("filename", None)
                if  file:
                    print(file.name)
                    # todo 这里可以增加文件格式校验
                    # 需要考虑处理文件重名的考虑
                    file_name = file.name.split('.')[0] + str(uuid.uuid1()).replace('-','') +'.'+ file.name.split('.')[1]
                    pathname = os.path.join('./files/upload/source/search', file_name)
                    print(pathname)
                    with open(pathname, 'wb+') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)

                    return JsonResponse(
                            {
                                'data':{
                                    'filename': file_name
                                },
                                'code': '000000',
                                'msg': '上传文件成功'
                            },
                            status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400000',
                            'msg': '上传文件失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'filename': 'This field is required.',
                        },
                        'code': '400001',
                        'msg': '上传文件失败'
                    },
                    status=200)

        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)

    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)


# 过滤等级和标签
#  条件是 version  module
@api_view(['POST'])
@csrf_exempt
def upload_download_script_file(request):
    try:
        if request.user.is_authenticated():
            if 'filename' in request.data:
                file = request.FILES.get("filename", None)
                if  file:
                    print(file.name)
                    # todo 这里可以增加文件格式校验
                    # 需要考虑处理文件重名的考虑
                    file_name = file.name.split('.')[0] + str(uuid.uuid1()).replace('-','') +'.'+ file.name.split('.')[1]
                    pathname = os.path.join('./files/upload/source/download', file_name)
                    print(pathname)
                    with open(pathname, 'wb+') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)

                    return JsonResponse(
                            {
                                'data':{
                                    'filename': file_name
                                },
                                'code': '000000',
                                'msg': '上传文件成功'
                            },
                            status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400000',
                            'msg': '上传文件失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'filename': 'This field is required.',
                        },
                        'code': '400001',
                        'msg': '上传文件失败'
                    },
                    status=200)

        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)

    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)



# 过滤等级和标签
#  条件是 version  module
@api_view(['POST'])
@csrf_exempt
def parse_file(request):
    try:
        if request.user.is_authenticated():
            # request.data['path'] = './files/upload/file.xlsx'
            if 'filename' in request.data:
                fh = FileHandler('./files/upload/' + str(request.data['filename']))
                rsp = fh.prase_excel_data()
                if rsp['flag']:
                    rsp = fh.save(request.user.id)
                    if rsp['flag']:
                        return JsonResponse(
                            {
                                'code': '000000',
                                'msg': rsp['msg']
                            },
                            status=200)
                    else:
                        return JsonResponse(
                            {
                                'data':rsp['data'],
                                'code': '400001',
                                'msg': rsp['msg']
                            },
                            status=200)
                else:
                    return JsonResponse(
                        {
                            'code': '400001',
                            'msg': rsp['msg']
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'filename': 'This field is required.',
                        },
                        'code': '400001',
                        'msg': '解析文件失败'
                    },
                    status=200)
        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)
    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)


# # 生成用例文件
# # 条件是 version  module
@api_view(['POST'])
@csrf_exempt
def generate_testcase(request):
    try:
        if request.user.is_authenticated():
            if 'version' in request.data:
                if 'module' in request.data:
                    tv = Testversion.objects.filter(id=request.data['version'])[0]
                    print(tv.version)
                    print(tv.client_type)

                    fh  = FileHandler()
                    file = fh.generate_file(request.data)
                    if  file['flag']:
                        return JsonResponse(
                                {
                                    'data': {
                                        'filename': file['filename']
                                        # 'items': file['items']
                                    },
                                    'code': '000000',
                                    'msg': '生成文件成功'
                                },
                                status=200)
                    else:
                        return JsonResponse(
                            {
                                'code': '400000',
                                'msg': file['msg']
                            },
                            status=400)
                else:
                    return JsonResponse(
                        {
                            'data': {
                                'module': 'This field is required.',
                            },
                            'code': '400001',
                            'msg': '生成文件失败'
                        },
                        status=200)
            else:
                return JsonResponse(
                    {
                        'data': {
                            'version': 'This field is required.',
                        },
                        'code': '400001',
                        'msg': '生成文件失败'
                    },
                    status=200)

        else:
            return JsonResponse(
                {
                    'code': '400000',
                    'msg': '无效的token'
                },
                status=401)
    except Exception as e:
        body = {
            'code':'400002',
            'msg':"接口"+ get_current_function_name() +"发生内部错误，并抛出异常"+ str(e),
        }
        return  JsonResponse(body, status=500)